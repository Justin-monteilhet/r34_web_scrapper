import requests as rq
import bs4
from PIL import Image
from tag import Tag
from datetime import datetime

class InvalidId(BaseException):
    def __init__(self, msg="The given ID is invalid"):
        self.msg = msg
        super().__init__(self.msg)

class Post(object):
    """Represents a rule 34 Post"""
    
    def __init__(self, post_id:str):
        """Init the post object

        Args:
            post_id (str): ID of the post

        Raises:
            InvalidId: Given ID does not exists (refer to Post.is_id_valid())
        """
        self.id = post_id
        url = f'https://rule34.xxx/index.php?page=post&id={post_id}&s=view'
        r = rq.get(url=url)
        self.code = r.status_code
        main_soup = bs4.BeautifulSoup(r.content, features="html.parser")
        self.full_html = main_soup
        self.img = main_soup.find('img', {'id':'image'})
        if not self.img:
            raise InvalidId()
        self.img_url = self.img['src']
        self.tags = [Tag(tag_name) for tag_name in self.img['alt'].split(' ')]
        tag_list = main_soup.find('ul', {'id':'tag-sidebar'})
        self.copyrights = [Tag(tag.a.text) for tag in tag_list.findAll('li', {'class':'tag-type-copyright'})]
        self.characters = [Tag(tag.a.text) for tag in tag_list.findAll('li', {'class':'tag-type-character'})]
        self.artists = [Tag(tag.a.text) for tag in tag_list.findAll('li', {'class':'tag-type-artist'})]
        stats_div = main_soup.find('div', {'id':'stats'})
        str_date = stats_div.findAll('li')[1].text.strip().split('\n')[0].replace('Posted: ', '')
        self.date = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
        source_tag = stats_div.find('a', {'rel':'nofollow'})
        self.source = source_tag['href'] if source_tag else None
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        if not self:
            return
        return f'<Post img_url={self.img_url}>'
    
    def get_image(self):
        """Gives a PIL object of the post image

        Returns:
            PIL.Image: The post image
        """
        return Image.open(rq.get(self.img_url, stream=True).raw)
        
    def get_metadata(self, keys:set=set()):
        """Gives the post metadata

        Args:
            keys (set, optional): Requested metadata. Defaults to all.

        Returns:
            dict: Metadata of the post
        """
        keys = set(keys)
        metadata = {'copyrights':self.copyrights, 
                    'artists':self.artists, 
                    'characters':self.characters, 
                    'tags':self.tags,
                    'source':self.source
        }
        if keys:
            return {k:v for k, v in metadata.items() if k in keys}
        
        else:
            return metadata
    
    @staticmethod
    def is_id_valid(post_id):
        """Checks if a post exists with its ID by finding img tag with id="image" in page HTML

        Args:
            post_id (str): ID of the post

        Returns:
            bool: True if the post exists
        """
        url = f'https://rule34.xxx/index.php?page=post&id={post_id}&s=view'
        r = rq.get(url=url)
        main_soup = bs4.BeautifulSoup(r.content, features="html.parser")
        img = main_soup.find('img', {'id':'image'})
        return not img == None
import requests as req
import bs4
from urllib.parse import quote
import time
import threading

from post import Post
from threads_request import threaded_request

class Query(object):
    def __init__(self):
        pass
    
    @staticmethod
    def query_by_tags(tags: set, pages: int = 1, anti_tags: set = set()):
        """Make a rule 34 Posts query by tags

        Args:

            tags (set{str}): Requested tags

            pages (int, optionnal): Number of pages to browse

            anti_tags (set, optionnal) : Tags to exclude from request

        Returns:
            Union(Post[], None): Found posts 
        """
        
        pages_url = list()
        posts_id = set()
        tags = {quote(tag.replace(' ', '_').lower()) for tag in tags}
        anti_tags = {'-'+quote(tag.replace(' ', '_').lower()) for tag in anti_tags}
        formatted_args = '+'.join(tags) + '+' + '+'.join(anti_tags)
        base_url = f"https://rule34.xxx/index.php?page=post&s=list&tags={formatted_args}"
        
        print(time.time(), 'Getting in all IDS...')
        start = time.time()
        for page_id in map(lambda x: x*42, range(pages)):
            page_url = base_url+f'&pid={page_id}'
            pages_url.append(page_url)

        def page_handler(page_url):
            page_soup = bs4.BeautifulSoup(req.get(page_url).content, features='html.parser')
            for thumbnail in page_soup.findAll('span', {'class':'thumb'}):
                post_id = thumbnail.a['id'][1:]
                if Post.is_id_valid(post_id):
                    posts_id.add(post_id)
        THREADS = []
        for url in pages_url:
            t = threading.Thread(target=page_handler, args=(url,))
            THREADS.append(t)
        
        for thread in THREADS:
            thread.start()
            
        for thread in THREADS:
            thread.join()
            
        print(time.time(), 'Done getting all IDs')
        print('Getting all ids took', time.time()-start, 's')
        return threaded_request(posts_id)

    @classmethod
    def query_by_artist(cls, name: str, **kwargs):
        """Make a rule 34 Posts query by artist name

        Args:

            name (str): Requested artist

            pages (int, optionnal): Number of pages to browse

            anti_tags (set, optionnal) : Tags to exclude from request

        Returns:
            Union(Post[], None): Found posts 
        """
        return cls.query_by_tags({name,}, **kwargs)
    
    @classmethod
    def query_by_characters(cls, names: tuple, **kwargs):
        """Make a rule 34 Posts query by artist name

        WARNING : Characters names might follow different schemes :
           * name
           * name_firstname
           * firstname_name
           * name_(work)
        
        Args:

            name (tuple): Requested characters

            pages (int, optionnal): Number of pages to browse

            anti_tags (set, optionnal) : Tags to exclude from request

        Returns:
            Union(Post[], None): Found posts 
        """
        names = tuple((names,))
        return cls.query_by_tags(set(names), **kwargs)
    
    @classmethod
    def query_by_work(cls, name: str, **kwargs):
        """Make a rule 34 Posts query by artist name

        WARNING : Characters names might follow different schemes :
           * name
           * name_firstname
           * firstname_name
           * name_(work)
        
        Args:

            name (tuple): Requested work

            pages (int, optionnal): Number of pages to browse

            anti_tags (set, optionnal) : Tags to exclude from request

        Returns:
            Union(Post[], None): Found posts 
        """
        names = tuple((name,))
        return cls.query_by_tags(set(names), **kwargs)
    
    @staticmethod
    def no_homo():
        """You'll thanks me later."""
        return {'yaoi', '1boy', 'male_only', 'gay', 'gay_sex', '2boys', 'femboy', 'genderswap', 'solo_male', 'futanari', 'futa_only', '1futa', 'male_on_futa', 'furry', 'eroborus', 'gachichan'}

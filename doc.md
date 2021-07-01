# Rule 34 API wrapper

This API is not made for all the user-side of the site. 

Its purpose is to deal with posts, tags, and artists.

# Data types

## Post

### Post(post_id) : Represents a rule 34 post
### id

str : Post id. 

Post ID is the number you can find on the post's statistic tab.

### img_url

str : URL of the post's image

### tags

List[Tag] : Every post's associated tags (general, artists, characters...)

### copyrights

List[Tag] : Works where the post is from (may be manga, video game, or Original Character)

### characters

List[Tag] : Characters involved in the post

### artists

List[Tag] : Creators of the post image. Not the post uploader.

### date

datetime.datetime : Upload date of the post

### source

Union(str, None) : Source of the post as a link, if specified.

### get_image -> *PIL.Image*
Returns the post picture

### get_metadata(keys=[]) -> *dict*
> keys -> Optionnal(Iterbale) : Requested metadata, default to all
>>
|Key| Description| type |
|- || |
|copyrigths| Works where the post is from| List[Tag] |
|artists|Creators of the post image.|List[Tag] |
|characters| Characters involved in the post|List[Tag]|
|tags|Every post's associated tags|List[Tag]|
|source|Source of the post as a lin|Union(str, None)| 

### is_id_valid(id) -> *bool*
> id -> str : Post ID

Staticmethod checking if a post exists with its ID.

## Tag
### Tag(name) : Represents a rule 34 tag
### Name
str : tag name
### url
str : tag's url (to get all posts with that tag)

## Query
### Query() : Represents a rule 34 query. Only has staticmethods.
### query_by_tags(tags, pages=1, anti_tags=set()) -> *Post[]*
Gives a Post list from tags

> tags -> set{str} : Requested tags

> pages -> Optionnal(int) : Number of pages to browse

> anti_tags -> Optionna(set) : Tags to exclude from request

**Returns ->** Union(Post[], None) : Found posts, None if none

### query_by_work(work:str, **kwargs) -> *Post[]*
### query_by_characters(names:list[str], **kwargs) -> *Post[]*
### query_by_artist(name:str, **kwargs) -> *Post[]*

Same as Query.query_by_tags but with different filters

## Test code - Image Downloader
```python
from r34_api.query import Query

q = Query.query_by_tags({'one piece', 'nami'}, pages=5, anti_tags={'futa'})
for index, post in enumerate(q):
    post.get_image().save(f'./images/{index}.png')
```

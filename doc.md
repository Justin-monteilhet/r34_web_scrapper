# Rule 34 API wrapper

This API is not made for all the user-side of the site. 

Its purpose is to deal with posts, tags, and artists.

# Data types

## Post

### id

str : Post Iid

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

### get_metadata(keys) -> *dict*
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
id -> str : Post ID

Staticmethod checking if a post exists with its ID.

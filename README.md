# Rule 34 API wrapper

Rule 34 API wrapper is a Python library for dealing with rule34 website posts, artists, and tags.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

## Documentation

Read the documentation [here](https://github.com/Justin-monteilhet/r34_api_wrapper/blob/main/doc.md).

```bash
pip install rule34-api-wrapper
```

## Usage
Basic query with tags as set. Queries return a list of Post objects.
```python
from r34_api import Query


q = Query.query_by_tags({'one piece', '1girl', 'juicy'})
```
You can specify pages

1 page = 42 posts
```python
q = Query.query_by_tags({'one piece',}, pages=5)
```
You can also specify anti-tags. Posts with these tags won't appear in results.
```python
q = Query.query_by_tags({'one piece',}, anti_tags={'furry',})
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

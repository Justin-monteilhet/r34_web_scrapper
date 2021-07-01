import requests as req
import bs4


class Tag(object):
    
    def __init__(self, name:str):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'<Tag name={self.name}>'
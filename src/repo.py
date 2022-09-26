from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    blog: str

class MemRepo:
    def __init__(self):
        self.db = []


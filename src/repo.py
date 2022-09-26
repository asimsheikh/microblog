from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    blog: str

class MemRepo:
    def __init__(self):
        self.db: list[Blog] = []

    def add_blog(self, blog: Blog):
        self.db.append(blog)

    def get_blogs(self) -> list[Blog]:
        return self.db


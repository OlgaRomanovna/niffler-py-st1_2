from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class Category(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    category: str
    username: str


class CategoryAdd(BaseModel):
    category: str
    username: str | None = None
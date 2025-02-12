"""
Pydantic schemas for news app
"""

from datetime import datetime

from pydantic import BaseModel


class NewsItemReadSchema(BaseModel):
    title: str
    content: str | None = None
    images: list[str | None]
    created: datetime
    updated: datetime
    category: str | None = None

    class Config:
        from_attributes = True 

class NewsReadSchema(BaseModel):
    id: int
    title: str
    created: datetime

    class Config:
         from_attributes = True 


class NewsCreateSchema(BaseModel):
    title: str
    content: str | None = None
    images: list[str | None]
    category: str | None = None


class CategoryReadSchema(BaseModel):
    """
    Category read schema
    """
    id: int
    name: str
    created: datetime

    class Config:
         from_attributes = True 


class CategoryCreateSchema(BaseModel):
    """
    Category create schema
    """
    name: str
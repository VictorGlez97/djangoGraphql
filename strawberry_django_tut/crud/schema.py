import datetime
from typing import List, Optional

import strawberry
import strawberry_django
from strawberry import auto

from .models import Book

from dataclasses import asdict

from asgiref.sync import sync_to_async

@strawberry.input
class BookInput:
    title: str
    author: str
    published_date: str

@strawberry_django.type(Book)
class BookType:
    id: auto
    title: auto
    author: auto
    published_date: auto

@strawberry_django.input(Book)
class BookUpdateInput:
    title: Optional[str] = None
    author: Optional[str] = None
    published_date: Optional[datetime.date] = None

@strawberry.type
class Query:
    books: List[BookType] = strawberry_django.field()

    @strawberry.field
    def all_books(self) -> List[BookType]:
        return Book.objects.all()


@strawberry.type
class Mutation:
    create_book: BookType = strawberry_django.mutations.create(BookInput)

    @strawberry.mutation
    async def update_book(self, book_id: int, data: BookUpdateInput) -> BookType:
        try:

            book = await sync_to_async(Book.objects.get)(id=book_id)

            for key, value in asdict(data).items():
                if value is not None:
                    setattr(book, key, value)

            await sync_to_async(book.save)()

            return book
        except Book.DoesNotExist:
            raise strawberry('Not found')
        
    @strawberry.mutation
    async def delete_book(self, book_id: int) -> bool:
        try:

            book = await sync_to_async(Book.objects.get)(pk=book_id)
            await sync_to_async(book.delete)()

            return True
        except Book.DoesNotExist:
            raise strawberry('Not found')

schema = strawberry.Schema(query=Query, mutation=Mutation)
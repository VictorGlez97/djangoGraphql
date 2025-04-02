import datetime
from typing import List, Optional

import strawberry
import strawberry_django
from strawberry import auto

from .models import Book

from dataclasses import asdict

from asgiref.sync import sync_to_async

import requests
import json
from dataclasses import asdict
import base64

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
class ResponseType:
    success: bool
    data: Optional[str] = None
    error: Optional[str] = None

@strawberry.input
class ParamsData:
    Nombre: str
    Paterno: str
    Materno: str
    Fecha: str

@strawberry.input
class DataFetch:
    FormatoArchivo: str
    Archivo: str
    parameters: Optional[ParamsData]
    reportDataSet: List[str]

@strawberry.type
class ResponseReport:
    Servicio: Optional[str]
    Mensaje: Optional[str]
    Message: Optional[str]
    Estatus: Optional[int]
    Data: str

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
        
    @strawberry.mutation
    async def fetch_endpoint(self, data: Optional[DataFetch]) -> str:
        try:

            urlToken = 'http://admin.bposspro.com:7849/identity/connect/token'

            headersToken = {'Content-Type': 'application/x-www-form-urlencoded'}

            payloadToken = {
                'client_id': '8e8c6bad8061deec8841fa8f910a1203',
                'scope': 'bps_api',
                'client_secret': 'dd58b6ca211a429250f5eed7701d4003',
                'grant_type': 'client_credentials'
            }

            responseToken = await sync_to_async(requests.post)(urlToken, data=payloadToken, headers=headersToken, timeout=60)
            responseToken.raise_for_status()

            ResponseType(success=True, data=responseToken.text)
            
            access_token = responseToken.json().get('access_token')

            if access_token:
                
                url = 'http://admin.bposspro.com:7849/api/v1.0/reporte/GenerarReporte'

                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                }

                jsonData = json.dumps(asdict(data))

                response = await sync_to_async(requests.post)(url, data=jsonData, headers=headers, timeout=60)
                response.raise_for_status()
                
                pdfBytes = base64.b64decode(response.json()['Data']).decode('utf-8')
                print(pdfBytes)

                with open('archivo_descarga.pdf', 'wb') as f:
                    f.write(base64.b64decode(pdfBytes))

                return ResponseType(success=True, data=pdfBytes)
        except requests.RequestException as e:
            return ResponseType(success=False, error=str(e))

schema = strawberry.Schema(query=Query, mutation=Mutation)
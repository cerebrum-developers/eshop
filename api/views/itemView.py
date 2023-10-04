from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.schemas import AutoSchema
from rest_framework.compat import coreapi, coreschema

from api.services.item import ItemService

itemService = ItemService()

item_schema = AutoSchema(manual_fields=[
    coreapi.Field(
        "item_name",
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        "price",
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        "stock",
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        "expiry_date",
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        "batch_number",
        required=True,
        location="form",
        schema=coreschema.String()
    ),
    coreapi.Field(
        "measurement_unit",
        required=True,
        location="form",
        schema=coreschema.String()
    )
])


class ItemCreateView(APIView):

    schema = item_schema

    def post(self, request, format=None):
        """
        Create Item
        """
        result = itemService.create(request, format=None)
        return Response(result, status= status.HTTP_200_OK)


class ItemUpdateView(APIView):

    schema = item_schema

    def put(self, request, pk, format= None):
        """
        Update Item
        """
        result = itemService.update(request, pk, format=None)
        return Response (result, status=status.HTTP_200_OK)


class ItemDetailView(APIView):

    def get(self, request, pk, format=None):
        """
        Get Details of Item
        """
        result = itemService.get_item(request, pk, format=None)
        return Response (result, status=status.HTTP_200_OK)


class ItemDeleteView(APIView):

    def delete(self,request, pk, format=None):
        """
        Delete Item
        """
        result = itemService.delete (request, pk, format=None)
        return Response (result, status=status.HTTP_200_OK)


class ItemListView(APIView):

    def get(self, request, format=None):
        """
        Get Item List
        """
        result = itemService.get_all_items (request, format=None)
        return Response (result, status=status.HTTP_200_OK)

class ItemListwithPagination(APIView):

    def post(self, request, format=None):
        """
        List with Pagination
        """
        result = itemService.get_items_with_pagination (request, format=None)
        return Response (result, status=status.HTTP_200_OK)
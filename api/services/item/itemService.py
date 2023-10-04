from .itemBaseService import *
from api.serializers.item import ItemSerializer,ItemSerializerPagination, ItemDetailSerializer
from rest_framework import status
from api.utils.messages.commonMessages import *
from api.utils.messages.itemMessages import *
from api.utils import CustomPagination

class ItemService(ItemBaseService):

    def create(self, request, format=None):
        """
        Create item
        """
        serializer = ItemSerializer (data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return ({"data": serializer.data, "code": status.HTTP_201_CREATED, "message": ITEM_CREATE})

        # if not valid
        return ({"data": serializer.errors, "code": status.HTTP_400_BAD_REQUEST, "message": BAD_REQUEST})

    def update(self, request, pk, format=None):
        """
        Update Item
        """
        item = self.get_object(pk)
        if item:
            data = request.data
            serializer = ItemSerializer(item, data=data)
            if serializer.is_valid ():
                serializer.save ()
                return ({"data": serializer.data, "code": status.HTTP_200_OK, "message":ITEM_UPDATED})
            else:
                return ({"data": serializer.errors, "code": status.HTTP_400_BAD_REQUEST, "message": BAD_REQUEST})
        else:
            return ({"data": None, "code": status.HTTP_400_BAD_REQUEST, "message": RECORD_NOT_FOUND})

    def get_item(self, request, pk, format=None ):
        """
        Item Retrieve
        """
        item = self.get_object(pk=pk)
        if item:
            serializer = ItemDetailSerializer(item)
            return ({"data": serializer.data, "code": status.HTTP_200_OK, "message": OK})

        return ({"data": None, "code": status.HTTP_400_BAD_REQUEST, "message": RECORD_NOT_FOUND})

    def delete(self, request, pk, format=None):
        """
        Item Delete
        """

        item = self.get_object(pk)
        if item:
            item.is_deleted = True
            item.is_active = False
            item.save()
            return ({"code": status.HTTP_200_OK, "message": ITEM_DELETED})
        else:
            return ({"code": status.HTTP_400_BAD_REQUEST, "message": RECORD_NOT_FOUND})

    def get_all_items(self, request, format=None):
        """
        Item List
        """
        items = Item.objects.filter(is_deleted=False)
        serializer = ItemSerializer (items, many=True)
        return ({"data": serializer.data, "code": status.HTTP_200_OK, "message": OK})


    def get_items_with_pagination(self, request, format=None):
        """
        Item List with Pagination
        """
        custom_pagination = CustomPagination()
        search_keys = ['item_name__contains', 'id__contains']
        search_type = 'or'

        items = Item.objects.filter(is_active =True ,is_deleted=False)

        items_response = custom_pagination.custom_pagination(request, Item, search_keys, search_type, ItemSerializerPagination, items)
        return {"data": items_response['response_object'],
                "recordsTotal": items_response['total_records'],
                "recordsFiltered": items_response['total_records'],
                "code": status.HTTP_200_OK, "message": OK}

    def get_object(self,pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return None
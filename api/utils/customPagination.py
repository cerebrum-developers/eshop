from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from math import ceil
import operator
from functools import reduce
from django.db.models import Q
import copy

class CustomPagination:

    def custom_pagination(self, request, model, search_keys, search_type, serializer, query, order_by=None):
        """ Function to handle custom pagination"""
        length = request.data['length']
        start = request.data['start']
        columns_order = request.data['order'][0]['column']
        order = request.data['columns'][columns_order]['data']
        direction = request.data['order'][0]['dir']
        search_value = request.data['search']['value']

        if (direction == 'desc'):
            order = '-' + order

        elif (order_by is not None and direction == 'undefined'):
            order = order_by

        elif (order_by is None and direction == 'undefined'):
            order = '-id'

        else:
            pass

        kwargs = []
        # print('\n\nquery')
        
        if (search_value):
            no_of_keys = len(search_keys)
            

            if no_of_keys > 0:
                for keyname in search_keys:
                    kwargs.append(Q(**{keyname:search_value}))

                if(search_type == 'and'):
                    query = query.filter(reduce(operator.and_, kwargs))
                else:
                    query = query.filter(reduce(operator.or_, kwargs))
        #else:
        #    query = model.objects.all()


        page_no = int(start/length + 1)
        query = query.order_by(order)
        paginator = Paginator(query, length)
        paginated_data = paginator.page(page_no)
        serializer = serializer(paginated_data, context={'request': request}, many=True)

        return {"response_object": serializer.data, "total_records": paginated_data.paginator.count}

    def custom_pagination_without_search(self, request, model, search_keys, search_type, serializer, query, order_by=None):
        """ Function to handle custom pagination"""
        length = request.data['length']
        start = request.data['start']
        columns_order = request.data['order'][0]['column']
        order = request.data['columns'][columns_order]['data']
        direction = request.data['order'][0]['dir']
        search_value = request.data['search']['value']

        if (direction == 'desc'):
            order = '-' + order

        elif (order_by is not None and direction == 'undefined'):
            order = order_by

        elif (order_by is None and direction == 'undefined'):
            order = '-id'

        else:
            pass

        
        page_no = int(start/length + 1)
        query = query.order_by(order)
        paginator = Paginator(query, length)
        paginated_data = paginator.page(page_no)
        serializer = serializer(paginated_data, many=True)

        return {"response_object": serializer.data, "total_records": paginated_data.paginator.count}

    def custom_pagination_for_search(self, request, search_keys, search_type, query):
        search_value = request.data['search']['value']

        kwargs = []
        new_queries = []
        if (search_value):
            for qr in query:
                if search_value.lower() in qr['name'].lower():
                    new_queries.append(qr)
        return new_queries


    def custom_pagination_for_therapist(self, request, start, length, query):
        query = query[start:start+length]
        return query

class CustomPaginationMobileView:

    def custom_pagination_mobile_view(self, request, model, search_keys, search_type, serializer, query, user=None):
        """
        Function to handle custom pagination for mobile view
        """

        length = request.data['length']

        start = request.data['start']

        page_no = int(int(start)/int(length) + 1)

        paginator = Paginator(query, length)


        try:
            paginated_data = paginator.page(page_no)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            paginated_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            return {"response_object": None, "total_records": 0}    


        serializer = serializer(paginated_data, context={'user': user}, many=True)

        return {"response_object": serializer.data, "total_records": paginated_data.paginator.count}


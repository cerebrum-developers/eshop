from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path ('item/create/', ItemCreateView.as_view(), name='item-create'),
    path ('item/detail/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path ('item/update/<int:pk>/', ItemUpdateView.as_view(), name='item-update'),
    path ('item/delete/<int:pk>/', ItemDeleteView.as_view(), name='item-delete'),
    path ('items/', ItemListView.as_view(), name='item-list'),
    path ('items-pagination/', ItemListwithPagination.as_view(), name='items-with-pagination'),
]
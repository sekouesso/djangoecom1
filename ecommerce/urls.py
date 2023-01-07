
from django.contrib import admin
from django.urls import path

from ecommerce.views import *

urlpatterns = [
    path('', index, name='index'),
    path('product/liste', liste_product, name='liste_product'),
    path('product/add', add_product, name='add_product'),
    path('product/<int:id>/update', update_product, name='update_product'),
    path('product/<int:id>/detail', detail_product, name='detail_product'),
    path('product/<int:id>/delete', delete_product, name='delete_product'),

    path('category/add', add_category, name='add_category'),
    path('category/search', search_categorie, name='search_category'),
    path('category/liste', liste_category, name='liste_category'),
    path('category/<int:id>/update', update_category, name='update_category'),
    path('category/<int:id>/detail', detail_category, name='detail_category'),
    path('category/<int:id>/delete', delete_category, name='delete_category'),

    path('client/add', add_client, name='add_client'),
    path('client/liste', liste_client, name='liste_client'),
    path('client/<int:id>/update', update_client, name='update_client'),
    path('client/<int:id>/detail', detail_client, name='detail_client'),
    path('client/<int:id>/delete', delete_client, name='delete_client'),

    path('fournisseur/add', add_fournisseur, name='add_fournisseur'),
    path('fournisseur/liste', liste_fournisseur, name='liste_fournisseur'),
    path('fournisseur/<int:id>/update', update_fournisseur, name='update_fournisseur'),
    path('fournisseur/<int:id>/detail', detail_fournisseur, name='detail_fournisseur'),
    path('fournisseur/<int:id>/delete', delete_fournisseur, name='delete_fournisseur'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

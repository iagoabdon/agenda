from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),  # type:ignore
    path('search/', views.search, name='search'), # type:ignore 
    path('', views.index, name='index'),  # type:ignore

   #### (Create)CRUD ####

     path('contact/create/', views.create, name='create'),  # type:ignore
]
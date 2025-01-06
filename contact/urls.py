from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),  # type:ignore
   
    path('search/', views.search, name='search'), # type:ignore 
    path('', views.index, name='index'),  # type:ignore

   #### contact (Create)CRUD ####

     path('contact/create/', views.create, name='create'),  # type:ignore
     path('contact/<int:contact_id>/update/', views.update, name='update'),
     path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

   ### crud 

    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
      

]  




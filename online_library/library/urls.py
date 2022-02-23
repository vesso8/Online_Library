# http://localhost:8000/ - home page
# http://localhost:8000/add/ - add book page
# http://localhost:8000/edit/:id - edit book page
# http://localhost:8000/details/:id - book details page
# http://localhost:8000/profile/ - profile page
# http://localhost:8000/profile/edit/ - edit profile page
# http://localhost:8000/profile/delete/ - delete profile page
from django.urls import path

from online_library.library.views import show_index, add_book, edit_book, show_details, show_profile, edit_profile, \
    delete_profile, create_profile, delete_book

urlpatterns = (
    path('', show_index, name='show index'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('delete/<int:pk>', delete_book, name='delete book'),
    path('details/<int:pk>/', show_details, name='show details'),
    path('profile/', show_profile, name='show profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

)
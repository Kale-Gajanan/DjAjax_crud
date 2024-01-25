"""djajax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


# myproject/urls.py
# myapp/urls.py
# myapp/urls.py
from django.urls import path
from ajaxdj.views import item_list, item_list_json, add_item, edit_item, delete_item, get_data, index, addnew, edit, \
    update, destroy, get_books, books, show, show1, book_detail, book_create, book_update, book_delete

urlpatterns = [
    path('item_list/', item_list, name='item_list'),
    path('item_list_json/', item_list_json, name='item_list_json'),
    path('add_item/', add_item, name='add_item'),
    path('edit_item/<int:item_id>/', edit_item, name='edit_item'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('ajax/get_data/', get_data, name='get_data'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('addnew',addnew, name='addnew'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', destroy, name='destroy'),
    path('get_books/', get_books, name='get_books'),
    path('books/', books, name='books'),
    path('show/', show, name='show'),
    path('show1/', show1, name='show1'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
    path('books/new/', book_create, name='book_create'),
    path('books/<int:pk>/edit/', book_update, name='book_update'),
    path('books/<int:pk>/delete/', book_delete, name='book_delete'),

]

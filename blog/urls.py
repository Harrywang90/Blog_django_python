

from django.urls import path
from . import views


urlpatterns = [

    path('index', views.blog),
    path('page/<int:page_id>', views.blog_page, name='page'),
    path('editor', views.edit_page, name='editor'),
    path('submit', views.sub_action, name='submittor'),
]

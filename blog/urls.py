from django.urls import path,include
from .views import home,contact,termins,blogs,blog_id
urlpatterns = [
    path('',home,name='home_page'),
    path('blogs/',blogs,name='blogs_page'),
    path('contact/',contact,name='contact_page'),
    path('termins/<int:page>/',termins,name='termins_page'),
    path('blog/<int:pk>/',blog_id,name='detail_page'),
]

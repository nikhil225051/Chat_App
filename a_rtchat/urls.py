from django.urls import path
from .views import *

urlpatterns =[
    path('',chat_view,name="home"),
    path('chat/room/<chatroom_name>', chat_view, name="chatroom"),
]
from django.urls import path

from reply.views import ReplyListAPI

app_name = 'reply'

urlpatterns = [
    path('list/', ReplyListAPI.as_view(), name='list')
]
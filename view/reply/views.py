from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from post.models import Post
from reply.models import Reply
from reply.serializers import ReplySerializer


# Create your views here.
class ReplyListAPI(APIView):
    def get(self, request):
        replies = Reply.objects.all()
        return Response(ReplySerializer(replies, many=True).data)


class ReplyWriteAPI(APIView):
    def post(self, request):
        datas = request.POST
        datas = {
            'post': Post.objects.get(id=datas['post_id']),
            'member': Member.objects.get(member_email=request.session['member_email']),
            'reply_content': datas['reply_content']
        }

        Reply.objects.create(**datas)


class ReplyUpdateAPI(APIView):
    def post(self, request):
        datas = request.POST

        Reply.objects.filter(id=datas['id']).update(reply_content=datas['reply_content'])


class ReplyDeleteAPI(APIView):
    def post(self, request):
        datas = request.POST
        Reply.objects.get(id=datas['id']).delete()
















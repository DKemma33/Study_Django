import math

from django.shortcuts import render, redirect
from django.views import View

from post.models import Post


# Create your views here.

# 게시글 목록
class PostListView(View):
    def get(self, request, page=1):
        size = 5
        offset = (page - 1) * size
        limit = page * size
        total = Post.objects.all().count()
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(total / size)
        endPage = realEnd if endPage > realEnd else endPage
        pageUnit = (page - 1 // 5) + 1
        if endPage == 0:
            endPage = 1

        context = {
            'posts': list(Post.objects.all())[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd
        }
        return render(request, 'post/list.html', context)
# [{id:1,post_title:'aaa'},{data},{data},{data},{data}]


# 게시글 작성
class PostWriteView(View):
    def get(self, request, page):
        return render(request, "post/write.html", {'member_name': '한동석', 'page': page})

    def post(self, request):
        datas = request.POST
        datas = {
            'post_title': datas['post_title'],
            'post_content': datas['post_content']
        }

        post = Post.objects.create(**datas)
        return redirect(post.get_absolute_url(1))


# 게시글 조회
class PostDetailView(View):
    def get(self, request, post_id, page):
        print(post_id)
        post = Post.objects.get(id=post_id)
        context = {
            'post': post,
            'page': page
        }
        return render(request, "post/detail.html", context)


# 게시글 수정
class PostUpdateView(View):
    def get(self, request, post_id, page):
        print(post_id)
        post = Post.objects.get(id=post_id)
        context = {'post': post, 'member_name': '한동석', 'page': page}
        # render(request, to, context): 바로 html 화면으로 이동
        return render(request, "post/update.html", context)

    def post(self, request, post_id, page):
        datas = request.POST
        datas = {
            'post_title': datas['post_title'],
            'post_content': datas['post_content']
        }
        Post.objects.update(**datas)
        # redirect(to): URL로 이동하여 다른 View에서 render()로 html 화면 이동
        return redirect(Post.objects.get(id=post_id).get_absolute_url(page))


# 게시글 삭제
class PostDeleteView(View):
    def get(self, request, post_id):
        Post.objects.get(id=post_id).delete()
        return redirect('post:list_init')
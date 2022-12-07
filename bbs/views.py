from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import Http404
from bbs.models import Board
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


# home 핸들러
def home(request, str):

    return HttpResponse(f"THIS IS {str}!!")


# 게시글 리스트 확인 페이지에서 사용할 클래스
class BoardListView(TemplateView):
    template_name = 'board_list.html'

    # 최초 1회
    queryset = Board.objects.all()

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.queryset

        queryset = Board.objects.all()

        return queryset

    def get(self, request, *args, **kwargs):
        # 해당 모델의 전체 데이터 얻어오기 (접속 시 마다)
        boards = self.get_object()

        # dict 자료형
        context = {
            'boards': boards
        }

        return self.render_to_response(context)


# 게시글 상세 페이지에서 사용할 클래스
class BoardDetailView(TemplateView):
    template_name = 'board_detail.html'
    queryset = Board.objects.all()
    pk_url_kwargs = 'board_id'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.queryset

        pk = self.kwargs.get(self.pk_url_kwargs)

        return queryset.filter(pk=pk).first()

    def get(self, request, *args, **kwargs):
        board = self.get_object()

        if not board:
            raise Http404('invalid board_id')

        context = {
            'board': board
        }

        return self.render_to_response(context)


# 게시글 생성에서 사용할 클래스
class BoardCreateView(TemplateView):
    template_name = 'board_create.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        post_data = {key: request.POST.get(key) for key in ('title', 'content', 'author')}

        for key in post_data:
            if not post_data[key]:
                raise Http404('No Data For {}'.format(key))

        board = Board.objects.create(title=post_data['title'], content=post_data['content'], author=post_data['author'])

        context = {
            'board': board
        }

        return HttpResponseRedirect(f"/board/{board.pk}")


# 게시글 수정에서 사용할 클래스
class BoardUpdateView(TemplateView):
    template_name = 'board_update.html'
    queryset = Board.objects.all()
    pk_url_kwargs = 'board_id'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.queryset

        pk = self.kwargs.get(self.pk_url_kwargs)

        return queryset.filter(pk=pk).first()

    def get(self, request, *args, **kwargs):
        context = {}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        post_data = {key: request.POST.get(key) for key in ('title', 'content', 'author')}

        for key in post_data:
            if not post_data[key]:
                raise Http404('No Data For {}'.format(key))

        board = self.get_object()

        if not board:
            raise Http404('invalid board_id')

        for key, value in post_data.items():
            setattr(board, key, value)

        board.save()

        context = {
            'board': board
        }

        return HttpResponseRedirect(f"/board/{board.pk}")


# 게시글 삭제에서 사용할 클래스
class BoardDeleteView(TemplateView):
    template_name = 'base.html'
    queryset = Board.objects.all()
    pk_url_kwargs = 'board_id'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.queryset

        pk = self.kwargs.get(self.pk_url_kwargs)

        return queryset.filter(pk=pk).first()

    def get(self, request, *args, **kwargs):
        board = self.get_object()

        if not board:
            raise Http404('invalid board_id')

        board.delete()

        return HttpResponseRedirect("/board/")

from django.shortcuts import render, redirect

from hellawapp.forms import BoardForm
from hellawapp.models import Board
#로그인
from django.contrib.auth.decorators import login_required


def hellaw_main(request):
    return render(request,'hellawapp/mainPage.html',{})

def board_postList(request): # 전체 게시글 조회
    boards = Board.objects.all()
    return render(request, 'hellawapp/board_list_test.html', {'boards': boards})

def board_detail(request, pk):
    board = Board.objects.get(id=pk)
    return render(request, 'hellawapp/board_detail.html',{'board': board})
@login_required
def board_post(request): # 게시글 작성
    if request.method == "POST": #post메서드
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            return redirect('board_postList') #작성 후 게시글 조회 페이지로 돌아가도록(그냥 괄호 안에 안 채워도 되나?)
    else:
        form = BoardForm()
    return render(request,'hellawapp/board_post.html', {'form':form})
@login_required
def board_edit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            return redirect('board_postList')
    else:
        form = BoardForm(instance=board)
    return render(request, 'hellawapp/board_post.html', {'form': form})
@login_required
def board_delete(request, pk): #글 작성자를 확인하여 지우는거 구현해야 함
    board = Board.object.get(id=pk)
    board.delete()
    return redirect('board_postList')



def search(request):
    boards = Board.objects.all().order_by('-id')

    q = request.POST.get('q', "")

    if q:
        boards = boards.filter(title__icontains=q)
        return render(request, 'hellawapp/search.html', {'boards': boards, 'q': q})

    else:
        return render(request, 'hellawapp/search.html')

def login(request):
    return render(request, 'hellawapp/login.html', {})

def login_update(request,pk):
    return render(request, 'hellawapp/login.html', {})
from django.shortcuts import render, redirect

from hellawapp.forms import BoardForm
from hellawapp.models import Board


def hellaw_main(request):
    return render(request,'hellawgapp/mainPage.html',{})

def board_postList(request): # 전체 게시글 조회
    boards = Board.objects.all()
    return render(request, 'hellawapp/board_list.html', {'boards': boards})

def board_detail(request, pk):
    board = Board.objects.get(id=pk)
    return render(request, 'hellawapp/board_detail.html',{'board': board})

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


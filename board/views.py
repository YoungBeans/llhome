from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Board

# Create your views here.

def board_create(request) :
    if request.method == 'POST' :
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        password = request.POST.get('pwd')

        if request.session.get('user') == False :
            return render(request, "main/home.html")
        
        user = request.session['user']

        board = Board (
            title = title,
            author = author,
            content = content,
            password = password,
            User_info = user
        )
        board.save()
        boards = Board.objects.all()
        context = {"boards" : boards}
        return render(request, "board/board_view.html", context)
    else :
        return render(request, "board/board.html")

def board_update(request, pk) :
    if request.POST.get("pwd") == Board.objects.get(pk=pk).password :
        if request.POST.get("title") and request.POST.get("author") and request.POST.get("content") :
            board = Board.objects.get(pk=pk)
            board.title = request.POST.get("title")
            board.author = request.POST.get("author")
            board.content = request.POST.get("content")
            board.save()
            return redirect('board', pk=board.id)
        else :
            board = Board.objects.get(pk = pk)
            context = {"board" : board}
            return render(request, "board/board.html", context)
    else :
        return redirect("board", pk=pk)
    
def board_delete(request, pk) :
    board = Board.objects.get(pk = pk)
    if request.POST.get("pwd") != board.password :
        return redirect(reverse("board"), pk=pk)
    board.delete()
    return redirect(reverse("board_view"))

def board_view(request) :
    if Board.objects.all() != None :
        boards = Board.objects.all()
        context = {"boards" : boards }
        return render(request, 'board/board_view.html', context)
    else :
        return render(request, 'board/board_view.html')

def board(request, pk) :
    board = Board.objects.get(pk=pk)
    context = {"board" : board}
    return render(request, "board/board_one.html", context)
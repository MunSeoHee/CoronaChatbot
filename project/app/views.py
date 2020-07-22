from django.shortcuts import render,redirect, get_object_or_404
from .models import Board
import datetime
# Create your views here.
def index(request):
    board = Board.objects
    return render(request, 'index.html', {'boards':board})

def read(request, board_id):
    read = get_object_or_404(Board, pk=board_id)
    return render(request, 'read.html', {'read':read})

def delete(request, board_id):
    ob = get_object_or_404(Board, pk=board_id)
    ob.delete()
    return redirect('/')

def update(request, board_id):
    ob = get_object_or_404(Board, pk=board_id)
    return render(request, 'update.html', {'ob':ob})

def up(request, board_id):
    ob = get_object_or_404(Board, pk=board_id)
    ob.title = request.GET['title']
    ob.text = request.GET['text']
    ob.category = request.GET['category']
    ob.date = datetime.datetime.now()
    ob.save()
    return redirect('/'+str(board_id))

def create(request):
    return render(request, 'new.html')

def new(request):
    ob = Board()
    ob.title = request.GET['title']
    ob.text = request.GET['text']
    ob.category = request.GET['category']
    ob.save()
    return redirect('/'+str(ob.id))
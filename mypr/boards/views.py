from django.http import HttpResponse
from .models import Board
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
def home(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)

'''def board_topics(request, pk):
        board = Board.objects.get(pk=pk)
        return render(request, 'topics.html', {'board': board})'''


def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'new_topic.html', {'board': board})

from django.shortcuts import render
def signup(request):
    return render(request, 'signup.html')
    #return HttpResponse("apple")
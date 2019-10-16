from django.shortcuts import render,redirect,get_object_or_404
from .forms import MovieForm,CommentForm
from .models import Movie

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context= {
        'movie':movie,
    }
    return render(request, 'index.html',context)

def create(request):
    if request.method == 'POST':
        form= MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
        
    context = {
        'form':form
    }
    return render(request,'form.html',context)

def detail(request, id):
    movie = get_object_or_404(Movie,id=id)
    context = {
        'movie':movie,
    }
    return render(request,'detail.html',context)

def create_comment(request,id):
    if request.method == 'POST':
        pass
    else:
        form = CommentForm()
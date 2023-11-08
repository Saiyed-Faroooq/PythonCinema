from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from .forms import MovieForm
# Create your views here.


def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def details(request, movie_id):
    mov = Movie.objects.get(id=movie_id)
    # return HttpResponse("This is Movie no. %s" % movie_id)
    return render(request, "detail.html", {"mov": mov})


def add_movie(request):
    if request.method == 'POST':
        nm = request.POST.get('name', )
        de = request.POST.get('des', )
        yr = request.POST.get('year', )
        img = request.FILES['img']
        mv = Movie(name=nm, des=de, year=yr, img=img)
        mv.save()
    return render(request, "add.html")

def update(request, id):
    mvfetch = Movie.objects.get(id=id)
    fmfetch = MovieForm(request.POST or None, request.FILES, instance=mvfetch)
    if fmfetch.is_valid():
        fmfetch.save()
        return redirect('/')
    return render(request, 'edit.html', {'fmfetch': fmfetch, 'mvfetch': mvfetch})


def delete(request, id):
    if request.method == 'POST':
        mvfetch = Movie.objects.get(id=id)
        mvfetch.delete()
        return redirect('/')
    return render(request, 'delete.html')

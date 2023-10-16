from django.shortcuts import redirect, render, get_object_or_404
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    movies = Movie.objects.all()

    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

@login_required
@require_http_methods(["GET","POST"])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    
    context = {
        'form': form
    }

    return render(request, 'movies/create.html', context)


@require_safe
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie':movie,
        'comment_form': comment_form,
        'comments': comments

    }
    return render(request,'movies/detail.html',context)


@login_required
@require_http_methods(["GET","POST"])
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user:
        if request.method == "POST":
            form = MovieForm(request.POST, instance = movie)
            if form.is_valid:
                form.save()
                return redirect("movies:detail",movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:detail', movie.pk)
    context = {
        'movie':movie,
        'form':form,
    }
    return render(request,"movies/update.html",context)


@require_POST
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if movie.user == request.user:
        movie.delete()
        return redirect("movies:index")
    else:
        return redirect("movies:detail", movie.pk)


def comments_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'movie': movie,
        'comment_form': comment_form
    }
    return render(request, 'movies/detail.html', context)



def comments_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', movie_pk)
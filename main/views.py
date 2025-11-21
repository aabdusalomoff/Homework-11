from django.shortcuts import render, redirect, get_object_or_404

from .models import Movie

def movie_list_view(request):
    movies = Movie.objects.filter(is_active=True).order_by('-created_at')
    return render(request,'index.html', {'movies':movies})

  
def movie_detail_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request,'detail.html', {'movie':movie})


def movie_delete_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "POST":
        movie.delete()
        return redirect("/")
    
    return render(request, 'delete.html', {'movie':movie})

def movie_create_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        poster = request.FILES.get('poster')
        
        movie = Movie.objects.create(
            title=title,
            desc=description,
            rejissor=genre,  
            image=poster
        )
        return redirect('movie_detail', pk=movie.pk)
    
    return render(request, 'create.html')


def movie_update_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    
    if request.method == "POST":
        movie.title = request.POST.get('title')
        movie.desc = request.POST.get('description')
        movie.rejissor = request.POST.get('genre')
        
        if request.FILES.get('poster'):
            movie.image = request.FILES.get('poster')
        
        movie.save()
        return redirect('movie_detail', pk=movie.pk)
    
    return render(request, 'update.html', {'movie': movie})



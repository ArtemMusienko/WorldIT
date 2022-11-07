from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

def news_home(request):
    search_query = request.GET.get('search', '')
    if search_query:
        news = Artiles.objects.filter(Q(title__icontains=search_query)
                                      | Q(anons__icontains=search_query))
    else:
        news = Artiles.objects.all()

    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'artile'

class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = Artiles
    template_name = 'news/update.html'

    form_class = ArtilesForm

    raise_exception = False

class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = Artiles
    success_url = '/news/'
    template_name = 'news/news-delete.html'

    raise_exception = False

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = ArtilesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, UserRegisterForm, UserLoginForm, SaleForm, UserUpdateForm, ProfileUpdateForm, PasswordChangingForm, PostSystemForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .models import VK, OneC, Discord, Telegram
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import PostSystem
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def telegram(request):
    return render(request, 'main/telegram.html')

def vk(request):
    return render(request, 'main/vk.html')

def oneC(request):
    return render(request, 'main/oneC.html')

def discord(request):
    return render(request, 'main/discord.html')

def comments(request):
    context = {
        'posts': PostSystem.objects.all()
    }
    return render(request, 'main/comments.html', context)

class PostListView(ListView):
    model = PostSystem
    template_name = 'main/comments.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = PostSystem

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostCreateView(LoginRequiredMixin, CreateView):
    model = PostSystem
    form_class = PostSystemForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostSystem
    form_class = PostSystemForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeletelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostSystem
    success_url = '/comments'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, "main/register.html", {"form": form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли')
            return redirect('home')
    else:
        form = UserLoginForm
    return render(request, "main/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Сотрудничество"
            body = {
                'name': form.cleaned_data['name'],
                'tema': form.cleaned_data['tema'],
                'number': form.cleaned_data['number'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'temich2001@yandex.ru',
                          ['worlditdiplom@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("contact")

    form = ContactForm()
    return render(request, "main/contact.html", {'form': form})

def index(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            subject = "Индивидуальный проект"
            body = {
                'name': form.cleaned_data['name'],
                'tema': form.cleaned_data['tema'],
                'number': form.cleaned_data['number'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'temich2001@yandex.ru',
                          ['worlditdiplom@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("/")

    form = SaleForm()
    return render(request, "main/index.html", {'form': form})

def profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'main/profile.html', context)

def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        messages.success(request, f'Ваш аккаунт успешно изменен!')
        return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': request.user
    }
    return render(request, 'main/profile_edit.html', context)

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'main/password_success.html', {})

def plDiscord(request):
    search_query = request.GET.get('Discord', '')
    p = Paginator(Discord.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    if search_query:
        n1 = Discord.objects.filter(Q(title__icontains=search_query) | Q(anons__icontains=search_query))
    else:
        n1 = Discord.objects.all()
    return render(request, "main/plDiscord.html", {'n1': n1, 'venues': venues})

def plOnec(request):
    search_query = request.GET.get('OneC', '')
    p = Paginator(OneC.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    if search_query:
        n2 = OneC.objects.filter(Q(title__icontains=search_query) | Q(anons__icontains=search_query))
    else:
        n2 = OneC.objects.all()
    return render(request, "main/plOneC.html", {'n2': n2, 'venues': venues})

def plVk(request):
    search_query = request.GET.get('VK', '')
    p = Paginator(VK.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    if search_query:
        n3 = VK.objects.filter(Q(title__icontains=search_query) | Q(anons__icontains=search_query))
    else:
        n3 = VK.objects.all()
    return render(request, "main/plVk.html", {'n3': n3, 'venues': venues})

def plTelegram(request):
    search_query = request.GET.get('telegram', '')
    p = Paginator(Telegram.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    if search_query:
        n4 = Telegram.objects.filter(Q(title__icontains=search_query) | Q(anons__icontains=search_query))
    else:
        n4 = Telegram.objects.all()
    return render(request, "main/plTelegram.html", {'n4': n4, 'venues': venues})

class VkDetailView(DetailView):
    model = VK
    template_name = 'main/details_vk.html'
    context_object_name = 'vk'

class TelegramDetailView(DetailView):
    model = Telegram
    template_name = 'main/details_telegram.html'
    context_object_name = 'telegram'

class OneCDetailView(DetailView):
    model = OneC
    template_name = 'main/details_oneC.html'
    context_object_name = 'oneC'

class DiscordDetailView(DetailView):
    model = Discord
    template_name = 'main/details_discord.html'
    context_object_name = 'discord'

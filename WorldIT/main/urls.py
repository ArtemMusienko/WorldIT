from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeletelView


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('comments', PostListView.as_view(), name='comments'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeletelView.as_view(), name='post-delete'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.register, name='register'),
    path('plDiscord', views.plDiscord, name='plDiscord'),
    path('plOnec', views.plOnec, name='plOnec'),
    path('plVk', views.plVk, name='plVk'),
    path('plTelegram', views.plTelegram, name='plTelegram'),
    path('login', views.user_login, name='login'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='main/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'),
         name='password_reset_complete'),
    path("contact", views.contact, name="contact"),
    path("vk", views.vk, name="vk"),
    path("oneC", views.oneC, name="oneC"),
    path("discord", views.discord, name="discord"),
    path("telegram", views.telegram, name="telegram"),
    path("profile", views.profile, name="profile"),
    path("profile_edit", views.profile_edit, name="profile_edit"),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='main/change-password.html')),
    path('password', PasswordsChangeView.as_view(template_name='main/change_password.html'), name='change_password'),
    path('password_success', views.password_success, name="password_success"),
    path('<int:pk>/details_vk', views.VkDetailView.as_view(), name='details_vk'),
    path('<int:pk>/details_telegram', views.TelegramDetailView.as_view(), name='details_telegram'),
    path('<int:pk>/details_oneC', views.OneCDetailView.as_view(), name='details_oneC'),
    path('<int:pk>/details_discord', views.DiscordDetailView.as_view(), name='details_discord'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

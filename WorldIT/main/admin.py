from django.contrib import admin
from .models import Profile, VK, Discord, Telegram, OneC, PostSystem

admin.site.register(Profile)
admin.site.register(VK)
admin.site.register(Discord)
admin.site.register(Telegram)
admin.site.register(OneC)
admin.site.register(PostSystem)

admin.site.site_header = 'Интернет-магазина WorldIT'

from django.contrib import admin
from .models import Article,Category,Comment,Bloger


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Bloger)


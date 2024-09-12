from django.contrib import admin

from .models import AttrTemplate, Template

admin.site.register(Template)

admin.site.register(AttrTemplate)
# Register your models here.

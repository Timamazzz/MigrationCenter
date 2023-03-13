from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AdditionalActivity)
admin.site.register(AreaOfActivity)
admin.site.register(Vacancy)


class DocImageAdmin(admin.StackedInline):
    model = DocImage


@admin.register(Document)
class PostAdmin(admin.ModelAdmin):
    inlines = [DocImageAdmin]
    model = Document

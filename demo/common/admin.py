from django.contrib import admin

from .models import Category, CLarge, CMedium, CSmall, TmpTest, TmpAdd

from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin

# @register(Category)
class CategoryAdmin(MaterialModelAdmin):
    list_display = ('large', 'medium', 'small')
    icon_name = 'library_books'
    search_fields = ('large', 'medium', 'small',)
    list_per_page = 10

@register(CLarge)
class CLargeAdmin(MaterialModelAdmin):
    list_display = ('name',)

@register(CMedium)
class CMediumAdmin(MaterialModelAdmin):
    list_display = ('categorylarge', 'name',)

@register(CSmall)
class CSmallAdmin(MaterialModelAdmin):
    list_display = ('categorylarge', 'categorymedium', 'name',)

class TmpAddInline(admin.TabularInline):
    model = TmpAdd
    ordering = ('id',)
    extra = 1

# @register(TmpTest)
class TmpTestAdmin(MaterialModelAdmin):
    list_display = ('choices1','choicesel',)
    if TmpTest.choicesel == '1':
        inlines = [TmpAddInline]

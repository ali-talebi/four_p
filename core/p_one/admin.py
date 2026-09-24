from django.contrib import admin
from django import forms
from .models import p1_methods, avamel, amel_score, Complexity,Frequnecy,Periority


@admin.register(p1_methods)
class p1_methods_admin(admin.ModelAdmin):
    fields = [('method_name','dimentions','score')]
    list_display = ['method_name','dimentions','score']
    list_filter = ['dimentions',]
    list_editable = ['dimentions',]


class ComplexityInline(admin.TabularInline):
    model = Complexity
    extra = 1


class FrequencyInline(admin.TabularInline):
    model = Frequnecy
    extra = 1


class PeriorityInline(admin.TabularInline):
    model = Periority
    extra = 1


class AmelScoreInline(admin.TabularInline):
    model = amel_score
    extra = 1


@admin.register(avamel)
class avamel_admin(admin.ModelAdmin):
    list_display = ['model_head', 'amel_name','self_score','relation_percent']
    list_filter  = ['model_head',]
    inlines = [ComplexityInline,FrequencyInline,PeriorityInline,AmelScoreInline]


@admin.register(Complexity)
class complexity_admin(admin.ModelAdmin):
    list_display = ['amel','complexity_name','complexity_description']
    list_filter  = ['amel',]
    list_display_links = ['amel',]
    # list_editable = ['amel',] 


@admin.register(Frequnecy)
class frequency_admin(admin.ModelAdmin):
    list_display = ['amel','frequency_name','frequency_description']
    list_filter  = ['amel',]
    list_display_links = ['amel',]
    # list_editable = ['amel',] 


@admin.register(Periority)
class periority_admin(admin.ModelAdmin):
    list_display = ['amel','periority_name','periority_description']
    list_filter  = ['amel',]
    list_display_links = ['amel',]
    # list_editable = ['amel',] 
    


@admin.register(amel_score)
class amel_score_admin(admin.ModelAdmin):
    list_display = ("name", "amel", "complexity", "frequency", "score")
    list_filter = ['amel',]
    list_editable = ["amel", "complexity", "frequency", "score"]
    search_fields = ("name", "amel__amel_name")



from django.contrib import admin
from django import forms
from .models import p1_methods, avamel, amel_score, Complexity,Frequnecy,Periority, TableGuide


@admin.register(p1_methods)
class p1_methods_admin(admin.ModelAdmin):
    fields = [('method_name','dimentions','score'),('complexity_level','frequency_level','importance_level')]
    list_display = ['method_name','dimentions','complexity_level','frequency_level','importance_level','score']
    list_filter = ['dimentions',]
    # list_editable = ['dimentions',]


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


@admin.register(TableGuide)
class TableGuide_admin(admin.ModelAdmin):
    fields = ['table_key','title','description']
    list_display = ['table_key','title','description']


@admin.register(avamel)
class avamel_admin(admin.ModelAdmin):
    fields = [('model_head','amel_name','self_score'),('definition',)]
    list_display = ['id','model_head', 'amel_name','self_score','relation_percent']
    list_filter  = ['model_head',]
    # list_display_links = ['id','model_head','amel_name']
    # inlines = [ComplexityInline,FrequencyInline,PeriorityInline,AmelScoreInline]


@admin.register(Complexity)
class complexity_admin(admin.ModelAdmin):
    fields = ['table_guide',('model_head','amel'),('complexity_name','title'),('short_definition'),('definition')]
    list_display = ['model_head','amel','complexity_name','title']
    list_filter  = ['model_head','amel','complexity_name']
    list_display_links = ['model_head','amel']
    # list_editable = ['amel',] 


@admin.register(Frequnecy)
class frequency_admin(admin.ModelAdmin):
    fields = ['table_guide',('model_head'),('frequency_name','title'),('definition')]
    list_display = ['model_head','frequency_name','title']
    list_filter  = ['model_head',]
    list_display_links = ['model_head','frequency_name']
    # list_editable = ['amel',] 


@admin.register(Periority)
class periority_admin(admin.ModelAdmin):
    fields = ['table_guide',('model_head'),('periority_name','title'),('definition')]
    list_display = ['model_head','title','definition']
    list_filter  = ['model_head',]
    list_display_links = ['model_head','title']
    # list_editable = ['amel',] 
    


@admin.register(amel_score)
class amel_score_admin(admin.ModelAdmin):
    fields = [('model_head','amel'),('complexity','frequency','periority','score')]
    list_display = ("model_head", "amel", "complexity","frequency", "periority", "score")
    list_filter = ['amel',]
    search_fields = ("name", "amel__amel_name")

    # @admin.display(description="نام عامل", ordering="amel__amel_name")
    # def get_amel_name(self, obj):
    #     return obj.amel.amel_name if obj.amel else "-"

    # @admin.display(description="نام فراوانی",ordering="frequency__title")
    # def get_frequency_name(self, obj):
    #     return obj.frequency.title if obj.amel else "-"

    # @admin.display(description="نام پیچیدگی",ordering="periority__title")
    # def get_periority_name(self, obj):
    #     return obj.periority.title if obj.amel else "-"

    # @admin.display(description="نام پیچیدگی",ordering="complexity__title")
    # def get_complexity_name(self, obj):
    #     return obj.complexity.title if obj.amel else "-"




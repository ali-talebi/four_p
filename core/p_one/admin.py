from django.contrib import admin
from .models import p1_methods, avamel, amel_score


@admin.register(p1_methods)
class p1_methods_admin(admin.ModelAdmin):
    list_display = ['method_name']


class AmelScoreInline(admin.TabularInline):
    model = amel_score
    extra = 1


@admin.register(avamel)
class avamel_admin(admin.ModelAdmin):
    list_display = ['model_head', 'amel_name']
    list_filter  = ['model_head',]
    inlines = [AmelScoreInline]


@admin.register(amel_score)
class amel_score_admin(admin.ModelAdmin):
    list_display = ['amel', 'complexity', 'frequency', 'score']
    list_filter = ['amel']
    list_editable = ['complexity', 'frequency', 'score']
    list_filter = ['amel','complexity','frequency']
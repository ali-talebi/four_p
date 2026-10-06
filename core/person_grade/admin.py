from django.contrib import admin
from .models import Person,person_grade_p_one,PersonFactorSelection
# Register your models here.



@admin.register(Person)
class Person_admin(admin.ModelAdmin):

    list_display = ['name','family','code_melli']
    search_fields = ['name','family','code_melli',]


class person_factor_selection(admin.TabularInline):
    model = PersonFactorSelection

@admin.register(person_grade_p_one)
class person_grade_p_one_admin(admin.ModelAdmin):
    list_display = ['human','model_head','get_total_scores']
    inlines = [person_factor_selection]


@admin.register(PersonFactorSelection)
class PersonFactorSelection_admin(admin.ModelAdmin):
    list_display = ['person_grade','model_head','amel','complexity','frequency','periority','get_score']

    # get_score.short_description = "امتیاز عامل"

    # @admin.display(description="امتیاز عامل")
    # def get_amel_score(self, obj):
    #     return obj.get_score()
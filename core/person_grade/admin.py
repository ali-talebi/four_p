from django.contrib import admin
from .models import Person,person_grade_p_one,PersonFactorSelection,Score_Grading_Arzi
# Register your models here.



@admin.register(Person)
class Person_admin(admin.ModelAdmin):

    list_display = ['name','family','code_melli']
    search_fields = ['name','family','code_melli',]


class person_factor_selection(admin.TabularInline):
    model = PersonFactorSelection

@admin.register(person_grade_p_one)
class person_grade_p_one_admin(admin.ModelAdmin):
    list_display = ['human','model_head','get_total_scores','get_masir_shoghli','get_grade_shoghli']
    inlines = [person_factor_selection]

    def get_masir_shoghli(self,obj):
        return obj.get_grading_arzi()[0]

    get_masir_shoghli.short_description = "مسیر شغلی"
    def get_grade_shoghli(self,obj):
        return obj.get_grading_arzi()[1]

    get_grade_shoghli.short_description = 'گرید شغلی'



@admin.register(PersonFactorSelection)
class PersonFactorSelection_admin(admin.ModelAdmin):
    list_display = ['person_grade','model_head','amel','complexity','frequency','periority','get_score']

    # get_score.short_description = "امتیاز عامل"

    # @admin.display(description="امتیاز عامل")
    # def get_amel_score(self, obj):
    #     return obj.get_score()

@admin.register(Score_Grading_Arzi)
class Score_Grading_Arzi_admin(admin.ModelAdmin):
    fields = [('masir_shoghli','grade_shoghli'),('min_score','mid_score','max_score')]
    list_display = ['masir_shoghli','grade_shoghli','min_score','mid_score','max_score']
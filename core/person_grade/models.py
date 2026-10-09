from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from p_one.models import p1_methods,Complexity,Frequnecy,Periority,avamel,amel_score
# Create your models here.



class Person(models.Model):

    name = models.CharField(verbose_name="نام",max_length=50)
    family = models.CharField(verbose_name="فامیلی",max_length=50)
    code_melli = models.CharField(verbose_name="کد ملی",max_length=11,unique=True)

    def __str__(self):
        return f'{self.name}-{self.family}-{self.code_melli}'

    class Meta:
        db_table = "person_table"
        verbose_name_plural = "افراد"


class person_grade_p_one(models.Model):
    human = models.OneToOneField(
        Person,
        verbose_name="فرد",
        on_delete=models.CASCADE
    )

    model_head = models.ForeignKey(
        p1_methods,
        verbose_name="روش گریدینگ",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f'{self.human}'



    def get_total_scores(self):
        sum = 0 
        total_factor_selection = self.factor_selections.all()
        print("total factor selection: ", total_factor_selection )
        for factor in total_factor_selection:
            sum += factor.get_score()

        return sum

    def get_grading_arzi(self):
        total_grading_arzi = Score_Grading_Arzi.objects.all()
        for grading_arzi in total_grading_arzi:
            if self.get_total_scores() <= grading_arzi.__dict__['max_score'] and self.get_total_scores() >= grading_arzi.__dict__['min_score'] :
                return grading_arzi.__dict__['masir_shoghli'],grading_arzi.__dict__['grade_shoghli']
        else:
            return 0,0
            
    class Meta:
        db_table = "person_grade_p_one_table"
        verbose_name = "گریدینگ شغلی فرد"
        verbose_name_plural = "گریدینگ شغلی افراد"

    
class PersonFactorSelection(models.Model):
    person_grade = models.ForeignKey(
        person_grade_p_one,
        verbose_name="گریدینگ فرد",
        related_name="factor_selections",
        on_delete=models.CASCADE
    )

    model_head = models.ForeignKey(
        p1_methods,
        verbose_name="روش گریدینگ",
        on_delete=models.PROTECT
    )

    amel = ChainedForeignKey(
        avamel,
        chained_field="model_head",
        chained_model_field="model_head",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name="عامل",
        on_delete=models.PROTECT
    )

    complexity = ChainedForeignKey(
        Complexity,
        chained_field="amel",
        chained_model_field="amel",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name="پیچیدگی",
        on_delete=models.PROTECT
    )

    frequency = ChainedForeignKey(
        Frequnecy,
        chained_field="model_head",
        chained_model_field="model_head",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name="فراوانی",
        on_delete=models.PROTECT
    )

    periority = ChainedForeignKey(
        Periority,
        chained_field="model_head",
        chained_model_field="model_head",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name="اهمیت",
        on_delete=models.PROTECT
    )

    def get_score(self):
        score_row = amel_score.objects.filter(
            model_head=self.person_grade.model_head,
            amel=self.amel,
            complexity=self.complexity,
            frequency=self.frequency,
            periority=self.periority,
        ).first()

        return score_row.score if score_row else 0

    class Meta:
        # db_table = "person_factor_selection_table"
        verbose_name_plural = "امتیاز دهی به عوامل"


class Score_Grading_Arzi(models.Model):

    masir_shoghli = models.PositiveSmallIntegerField(verbose_name="مسیر شغلی")
    grade_shoghli = models.PositiveSmallIntegerField(verbose_name="گرید شغلی")
    min_score = models.PositiveSmallIntegerField(verbose_name="min")
    mid_score = models.PositiveSmallIntegerField(verbose_name="mid")
    max_score = models.PositiveSmallIntegerField(verbose_name="max")


    def __str__(self):
        return f'{self.masir_shoghli}-{self.grade_shoghli}'

    class Meta:
        db_table = "grade_arzi_table"
        verbose_name_plural = "امتیازات گردینگ عرضی"
    



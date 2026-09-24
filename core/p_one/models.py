from django.db import models
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.

class p1_methods(models.Model):

    dimention_level = (
        ('2D','2D'),
        ('3D','3D')
    )


    method_name = models.CharField(verbose_name="نام روش",max_length=20)
    score = models.IntegerField(verbose_name="مجموع امتیاز",null=True,blank=True)
    dimentions = models.CharField(verbose_name="ابعاد این روش",max_length=10,choices =dimention_level,null=True)
    def __str__(self):
        return f'{self.method_name} - {self.dimentions}'


    class Meta:
        db_table = 'table_p1_method'
        verbose_name_plural = 'نام روشها در گردینگ شغلی'




class avamel(models.Model):

    model_head = models.ForeignKey(p1_methods,verbose_name="مدل ارزشیابی",related_name="avamels",on_delete=models.PROTECT)
    amel_name = models.CharField(verbose_name="نام عامل",max_length=200)
    self_score = models.IntegerField(verbose_name="امتیاز این عامل",null=True,blank=True)



    def get_method_score(self):
        return self.model_head.score

    @property
    def relation_percent(self):
        if not self.self_score or not self.get_method_score():
            return 0

        return round((self.self_score / self.get_method_score()) * 100,2)


    def __str__(self):
        return f'{self.model_head} - {self.amel_name}'

    class Meta:
        db_table = 'table_avamels'
        verbose_name_plural = 'عوامل در روشهای ارزشیابی'



class Complexity(models.Model):
    
    amel = models.ForeignKey(avamel,on_delete=models.CASCADE,related_name="complexities")
    complexity_name = models.CharField(verbose_name="نام سطح پیچیدگی",max_length=50)
    complexity_description = models.TextField(verbose_name="توضیحات")


    def __str__(self):
        return f'{self.amel} - {self.complexity_name}'

    class Meta:
        verbose_name_plural = 'پیچیدگی'
        db_table = "table_complexity"



class Frequnecy(models.Model):

    amel = models.ForeignKey(avamel,on_delete=models.CASCADE,related_name="frequencies")
    frequency_name = models.CharField(verbose_name="نام سطح فراوانی",max_length=50)
    frequency_description = models.TextField(verbose_name="توضیحات")


    def __str__(self):
        return f'{self.amel} - {self.frequency_name}'

    class Meta:
        verbose_name_plural = 'فراوانی'
        db_table = "table_frequency"



class Periority(models.Model):
    amel = models.ForeignKey(avamel,on_delete=models.CASCADE,related_name="periorites")
    periority_name = models.CharField(verbose_name="نام سطح اهمیت")
    periority_description = models.TextField(verbose_name="توضیحات")

    def __str__(self):
        return f'{self.amel} - {self.periority_name}'

    class Meta:
        verbose_name_plural = 'اهمیت'
        db_table = "table_periority"
    


class amel_score(models.Model):
    amel = models.ForeignKey(
        avamel, verbose_name="عامل", on_delete=models.PROTECT, related_name="scores"
    )
    name = models.CharField(verbose_name="نام سطح امتیاز", max_length=20)
    description = models.TextField(
        verbose_name="توضیحات", blank=True, null=True
    )

    # اتصال به مدل Complexity وابسته به amel انتخاب شده
    complexity = ChainedForeignKey(
        Complexity,
        chained_field="amel",  # نام فیلد والد در همین مدل
        chained_model_field="amel",  # نام فیلد ارتباطی در مدل Complexity
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name="پیچیدگی",
        on_delete=models.PROTECT,
    )

    # اتصال به مدل Frequnecy وابسته به amel انتخاب شده
    frequency = ChainedForeignKey(
        Frequnecy,
        chained_field="amel",
        chained_model_field="amel",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name="فراوانی",
        on_delete=models.PROTECT,
    )

    # اتصال به مدل Periority وابسته به amel انتخاب شده
    periority = ChainedForeignKey(
        Periority,
        chained_field="amel",
        chained_model_field="amel",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name="اهمیت",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    score = models.IntegerField(verbose_name="امتیاز")

    def __str__(self):
        return f"{self.amel} - {self.name}"

    class Meta:
        db_table = "table_amel_score"
        verbose_name_plural = "امتیازدهی به عوامل"









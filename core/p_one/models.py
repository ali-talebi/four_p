from django.db import models

# Create your models here.

class p1_methods(models.Model):

    method_name = models.CharField(verbose_name="نام روش",max_length=20)

    def __str__(self):
        return f'{self.method_name}'


    class Meta:
        db_table = 'table_p1_method'
        verbose_name_plural = 'نام روشها در گردینگ شغلی'




class avamel(models.Model):

    model_head = models.ForeignKey(p1_methods,verbose_name="مدل ارزشیابی",related_name="avamels",on_delete=models.PROTECT)
    amel_name = models.CharField(verbose_name="نام عامل",max_length=50)

    def __str__(self):
        return f'{self.model_head} - {self.amel_name}'

    class Meta:
        db_table = 'table_avamels'
        verbose_name_plural = 'عوامل در روشهای ارزشیابی'


class amel_score(models.Model):
    
    amel = models.ForeignKey(avamel,verbose_name="عامل",on_delete=models.PROTECT,related_name="scores")
    name = models.CharField(verbose_name="نام  سطح امتیاز",max_length=20)
    description = models.TextField(verbose_name="توضیحات")
    complexity  = models.SmallIntegerField(verbose_name="‍پیچیدگی")
    frequency = models.SmallIntegerField(verbose_name="فراوانی")
    score = models.IntegerField(verbose_name="امتیاز")


    def __str__(self):
        return f'{self.amel} - {self.name}'
    
    class Meta:
        db_table = 'table_amel_score'
        verbose_name_plural = 'امتیازدهی به عوامل'







from django.db import models
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.

class p1_methods(models.Model):

    dimention_level = (
        ('2D','2D'),
        ('3D','3D')
    )


    method_name = models.CharField(verbose_name="نام روش",max_length=20)
    score = models.IntegerField(verbose_name="مجموع امتیاز")
    dimentions = models.CharField(verbose_name="ابعاد این روش",max_length=10,choices =dimention_level,null=True)
    complexity_level = models.PositiveSmallIntegerField(verbose_name="تعداد سطوح پیچیدگی")
    frequency_level  = models.PositiveSmallIntegerField(verbose_name="تعداد سظوح فراوانی")
    importance_level = models.PositiveSmallIntegerField(verbose_name="تعداد سطوح اهمیت")

    
    def __str__(self):
        return f'{self.method_name}-{self.dimentions}-{self.complexity_level}-{self.frequency_level}-{self.importance_level}'


    class Meta:
        db_table = 'table_p1_method'
        verbose_name_plural = 'نام روشها در گردینگ شغلی'



class avamel(models.Model):

    model_head = models.ForeignKey(p1_methods,verbose_name="مدل ارزشیابی",related_name="avamels",on_delete=models.PROTECT)
    amel_name = models.CharField(verbose_name="نام عامل",max_length=200)
    self_score = models.PositiveSmallIntegerField(verbose_name="امتیاز این عامل")
    definition = models.TextField(verbose_name="تعریف عامل")



    def get_method_score(self):
        return self.model_head.score

    @property
    def relation_percent(self):
        if not self.self_score or not self.get_method_score():
            return 0

        return round((self.self_score / self.get_method_score()) * 100,2)


    def __str__(self):
        return f'{self.amel_name}'
 
    class Meta:
        db_table = 'table_avamels'
        verbose_name_plural = 'عوامل در روشهای ارزشیابی'





class TableGuide(models.Model):
    TABLE_CHOICES = (
        ('complexity', 'جدول سطوح پیچیدگی'),
        ('periority', 'جدول سطوح اهمیت'),
        ('frequency', 'جدول سطوح فراوانی'),
        ('avamel', 'جدول عوامل ارزیابی'),
        ('methods', 'جدول روش‌های ارزیابی'),
    )

    table_key = models.CharField(
        max_length=50, 
        choices=TABLE_CHOICES, 
        unique=True, 
        verbose_name="شناسه جدول"
    )
    title = models.CharField(
        max_length=150, 
        verbose_name="عنوان فارسی جدول"
    )
    description = models.TextField(
        verbose_name="توضیحات و تعریف کلی جدول"
    )

    def __str__(self):
        return f"{self.title} ({self.table_key})"

    class Meta:
        db_table = "table_guide"
        verbose_name = "راهنمای جدول"
        verbose_name_plural = "راهنمای جداول"



class Complexity(models.Model):
    table_guide = models.ForeignKey(TableGuide,verbose_name="توضیح جدول",on_delete=models.PROTECT)
    model_head = models.ForeignKey(p1_methods,verbose_name="مدل ارزشیابی",on_delete=models.PROTECT)
    amel = ChainedForeignKey(
        avamel,
        chained_field="model_head",
        chained_model_field="model_head",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name="عامل",
        on_delete=models.PROTECT,
        
    )

    complexity_name = models.CharField(verbose_name="سطح",max_length=50)
    title = models.CharField(verbose_name="عنوان",max_length=50)
    short_definition = models.CharField(verbose_name="تعریف کوتاه",max_length=250,null=True)
    definition = models.TextField(verbose_name="تعریف بلند")


    def __str__(self):
        return f'{self.complexity_name}'

    class Meta:
        verbose_name_plural = 'پیچیدگی'
        db_table = "table_complexity"



class Frequnecy(models.Model):
    table_guide = models.ForeignKey(TableGuide,verbose_name="توضیح جدول",on_delete=models.PROTECT)
    model_head = models.ForeignKey(p1_methods,verbose_name="مدل ارزشیابی",on_delete=models.CASCADE,related_name="frequencies")
    frequency_name = models.CharField(verbose_name="نام سطح فراوانی",max_length=50)
    title = models.CharField(verbose_name="عنوان",max_length=200)
    definition = models.TextField(verbose_name="تعریف")


    def __str__(self):
        return f'{self.frequency_name}'

    class Meta:
        verbose_name_plural = 'فراوانی'
        db_table = "table_frequency"



class Periority(models.Model):
    table_guide = models.ForeignKey(TableGuide,verbose_name="توضیح جدول",on_delete=models.PROTECT)
    model_head = models.ForeignKey(p1_methods,verbose_name="مدل ارزشیابی",on_delete=models.CASCADE,related_name="periorites")
    periority_name = models.CharField(verbose_name="نام سطح اهمیت")
    title = models.CharField(verbose_name="عنوان",max_length=200)

    definition = models.TextField(verbose_name="تعریف")

    def __str__(self):
        return f'{self.periority_name}'

    class Meta:
        verbose_name_plural = 'اهمیت'
        db_table = "table_periority"
    


class amel_score(models.Model):
    
    model_head = models.ForeignKey(p1_methods,verbose_name="روش ارزشیابی",on_delete=models.PROTECT)

    amel = ChainedForeignKey(
        avamel,
        chained_field="model_head",  
        chained_model_field="model_head",  
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name="عامل",
        on_delete=models.PROTECT,
        related_name="amel_scores"
    )


    complexity = ChainedForeignKey(
        Complexity,
        chained_field="amel",  
        chained_model_field="amel",  
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name="سطح پیچیدگی",
        on_delete=models.PROTECT,
        related_name="complexities_scores"
    )

    frequency = models.ForeignKey(Frequnecy,on_delete=models.PROTECT,verbose_name="سطح فراوانی")

    periority = models.ForeignKey(Periority,on_delete=models.PROTECT,verbose_name="سطح اهمیت")

    score = models.PositiveSmallIntegerField(verbose_name="امتیاز")

    def __str__(self):
        return f"{self.amel}-{self.complexity}-{self.frequency}-{self.periority}-{self.score}"

    class Meta:
        db_table = "table_amel_score"
        verbose_name_plural = "امتیازدهی به عوامل"









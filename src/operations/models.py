from django.db import models
from utils.models import BaseModel, DateModel, Deletable


class IncomeCategory(models.Model):
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Категория дохода"
        verbose_name_plural = "Категории доходов"

    def __str__(self):
        return f'{self.name}'


class IncomeSubcategory(models.Model):
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Субкатегория дохода"
        verbose_name_plural = "Субкатегории доходов"

    def __str__(self):
        return f'{self.name}'


class OutcomeCategory(models.Model):
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Категория расхода"
        verbose_name_plural = "Категории расходов"

    def __str__(self):
        return f'{self.name}'


class OutcomeSubcategory(models.Model):
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Субкатегория расхода"
        verbose_name_plural = "Субкатегории расходов"

    def __str__(self):
        return f'{self.name}'


class Income(BaseModel, DateModel, Deletable):
    """
        Доход
    """

    category = models.ForeignKey(
        IncomeCategory,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    subcategory = models.ForeignKey(
        IncomeSubcategory,
        verbose_name="Субатегория",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание", null=True, blank=True)
    amount = models.FloatField("Сумма")
    is_paid = models.BooleanField("Оплачено", default=False)

    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'

    def __str__(self):
        return f'{self.title}'


class Outcome(BaseModel, DateModel, Deletable):
    """
        Расход
    """

    category = models.ForeignKey(
        OutcomeCategory,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    subcategory = models.ForeignKey(
        OutcomeSubcategory,
        verbose_name="Субатегория",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание", null=True, blank=True)
    amount = models.FloatField("Сумма")
    is_paid = models.BooleanField("Оплачено", default=False)

    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'

    def __str__(self):
        return f'{self.title}'

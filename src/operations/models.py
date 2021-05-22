from django.db import models
from utils.models import BaseModel, DateModel, Deletable
from django.contrib.auth.models import User

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


class Customer(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", null=True, blank=True)
    phone = models.TextField("Описание", null=True, blank=True)
    email = models.TextField("Описание", null=True, blank=True)
    website = models.TextField("Описание", null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        verbose_name = "Покупатель проекта"
        verbose_name_plural = "Покупатели проекта"

    def __str__(self):
        return f'{self.name}'



class Projects(BaseModel, DateModel, Deletable):
    """
        Проект
    """

    customer = models.ForeignKey(
        Customer,
        verbose_name="Покупатель",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    developers = models.ManyToManyField(User)
    payments = models.ManyToManyField(Income)
    expences = models.ManyToManyField(Outcome)

    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание", null=True, blank=True)
    technical_task = models.FileField(upload_to='files/tasks', blank=True)
    price = models.FloatField("Цена")
    status = models.CharField("Статус", max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_delated = models.BooleanField("Оплачено", default=False)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'{self.title}'
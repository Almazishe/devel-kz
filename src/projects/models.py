from django.db import models
from utils.models import BaseModel, DateModel, Deletable
from django.contrib.auth import get_user_model
from operations.models import Income, Outcome


# Create your models here.
class Customer(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", null=True, blank=True)
    phone = models.CharField("Телефон", max_length=12)
    email = models.EmailField("Почта", null=True, blank=True)
    website = models.CharField("Веб-сайт", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Покупатель проекта"
        verbose_name_plural = "Покупатели проекта"

    def __str__(self):
        return f'{self.name}'


class Projects(models.Model):
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
    developers = models.ManyToManyField(get_user_model())
    payments = models.ManyToManyField(Income)
    expences = models.ManyToManyField(Outcome)

    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание", null=True, blank=True)
    technical_task = models.FileField(upload_to='files/project_tasks', blank=True)
    price = models.FloatField("Цена")
    status = models.CharField("Статус", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delated = models.BooleanField("Оплачено", default=False)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'{self.title}'

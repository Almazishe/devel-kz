from django.db import models
from utils.models import BaseModel, DateModel, Deletable
from django.contrib.auth import get_user_model
from operations.models import Income, Outcome


# Create your models here.
class Customer(DateModel, Deletable):
    """
        Модель заказщика со всеми имеющимися контактыми данными
    """

    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", blank=True, default='')
    phone = models.CharField("Телефон", max_length=12, blank=True)
    email = models.EmailField("Почта", blank=True)
    website = models.CharField("Веб-сайт", max_length=255, blank=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f'{self.name}'


class Project(BaseModel, DateModel, Deletable):
    """
        Проект
    """
    PROCESSING = 'PR'
    UNDER_DEV = 'UD'
    FINISHED = 'FN'

    PROJECT_CTATUS_CHOICES = [
        (PROCESSING, 'Processing'),
        (UNDER_DEV, 'Under development'),
        (FINISHED, 'Finished'),
    ]

    customer = models.ForeignKey(
        Customer,
        verbose_name="Покупатель",
        on_delete=models.SET_NULL,
        null=True
    )
    developers = models.ManyToManyField(get_user_model(), blank=True, related_name='project')
    payments = models.ManyToManyField(Income, blank=True, related_name='project')
    expences = models.ManyToManyField(Outcome, blank=True, related_name='project')

    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание", blank=True, default='')
    technical_task = models.FileField(upload_to='files/project_tasks', blank=True)
    status = models.CharField("Статус", choices=PROJECT_CTATUS_CHOICES, max_length=2)
    price = models.FloatField("Цена")

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'{self.title}'

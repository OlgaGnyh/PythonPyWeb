from django.db import models
from django.core.validators import RegexValidator
from datetime import date, datetime, timezone


class TypeTrans(models.Model):
    type_trans_shot = models.CharField(max_length=5,
                                       unique=True,
                                       verbose_name="Краткое название вида транспорта",
                                       help_text="Краткое название вида транспорта, уникальное. Ограничение 5 знаков ")
    type_trans = models.CharField(max_length=50,
                                  unique=True,
                                  verbose_name="Вид транспорта",
                                  help_text="Вид транспорта, уникальное. Ограничение 50 знаков")
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания объекта сущности в базе данных
    updated_at = models.DateTimeField(auto_now=True)  # Дата и время обновления объекта сущности в базе данных

    def __str__(self):
        return f"Тип транспорта: {self.type_trans}"


class TypeVehicle(models.Model):
    type_vehicle_shot = models.CharField(max_length=10,
                                         unique=True,
                                         verbose_name="Краткое название типа подвижного состава",
                                         help_text="Краткое название типа подвижного состава, уникальное. Ограничение 10 знаков")
    type_vehicle = models.CharField(max_length=50,
                                    unique=True,
                                    verbose_name="Тип подвижного состава",
                                    help_text="Тип подвижного состава, уникальное. Ограничение 50 знаков")
    capacity = models.IntegerField(verbose_name="Вместимость подвижного состава",
                                   help_text="Вместимость подвижного состава")
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания объекта сущности в базе данных
    updated_at = models.DateTimeField(auto_now=True)  # Дата и время обновления объекта сущности в базе данных

    def __str__(self):
        return f"Тип подвижного состава: {self.type_vehicle}"


class Carriers(models.Model):
    name_carrier = models.CharField(max_length=100,
                                    unique=True,
                                    verbose_name="Наименование перевозчика",
                                    help_text=" Наименование перевозчика уникальное. Ограничение 100 знаков")
    address = models.TextField(verbose_name='Адрес',
                               help_text="Введите адрес.",
                               null=True,
                               blank=True,
                               )
    name_director = models.CharField(max_length=50,
                                unique=True,
                                verbose_name="Начальник",
                                help_text="ФИО начальника . Ограничение 50 знаков")
    phone_regex = RegexValidator(
        regex=r'^\+79\d{9}$',
        message="Номер телефона должен быть в формате: '+79123456789'."
    )
    phone_number = models.CharField(validators=[phone_regex],
                                    max_length=12,
                                    blank=True,
                                    null=True,
                                    unique=True,
                                    help_text="Формат +79123456789",
                                    )  # максимальная длина 12 символов
    email = models.EmailField(verbose_name='Адрес электронной почты',
                              help_text="Адрес почты в формате *@*.*")
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания объекта сущности в базе данных
    updated_at = models.DateTimeField(auto_now=True)  # Дата и время обновления объекта сущности в базе данных

    def __str__(self):
        return f"Перевозчик: {self.name_carrier}"


class Routes(models.Model):
    type_trans = models.ForeignKey(TypeTrans, on_delete=models.CASCADE, related_name="trans", )
    number_route = models.CharField(max_length=10,
                                    verbose_name="Номер маршрута",
                                    help_text="Номер маршрута")
    name_route = models.CharField(max_length=100,
                                  verbose_name="Название маршрута",
                                  help_text=" Название маршрута")
    type_vehicle = models.ForeignKey(TypeVehicle, on_delete=models.CASCADE, related_name="vehicles")
    type_tariff = models.CharField(max_length=2,
                                   choices=[('р', 'регулируемый'), ('нр', 'нерегулируемый')],
                                   verbose_name='Тип тарифа',
                                   help_text="Выберите тип тарифа",
                                   null=True,
                                   blank=True, )
    length = models.DecimalField(max_digits=4, decimal_places=1)
    carrier = models.ForeignKey(Carriers, on_delete=models.CASCADE, related_name="carriers")
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания объекта сущности в базе данных
    updated_at = models.DateTimeField(auto_now=True)  # Дата и время обновления объекта сущности в базе данных

    def __str__(self):
        return f"Маршрут номер №{self.number_route} - {self.name_route}"

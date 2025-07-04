
from django.db import models


class Author(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия"
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения",
    )
    biography = models.TextField(
        verbose_name="Автобиография",
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

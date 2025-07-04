from django.db import models

from autor.models import Author

# Create your models here.
class Books(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name="Автор"
    )
    title = models.CharField(
        max_length=200,
        verbose_name="Название книги",
        db_index=True
    )
    publish_year = models.PositiveIntegerField(
        verbose_name="Год издания",
        db_index=True
    )
    preface = models.TextField(
        verbose_name="Предисловие",
        blank=True,
        null=True
    )
    cover = models.ImageField(
        verbose_name="Обложка",
        upload_to='book_covers/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.title} ({self.publish_year})"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

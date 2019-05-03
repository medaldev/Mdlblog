from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(max_length=10000, verbose_name='Текст')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"


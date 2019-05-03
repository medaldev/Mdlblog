from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(max_length=10000, verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Post(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(max_length=10000, verbose_name='Текст')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

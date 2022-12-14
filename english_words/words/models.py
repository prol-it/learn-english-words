from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Dictionaries(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Словарь'
        verbose_name_plural = 'Словари'

    def __str__(self):
        return self.name


class Words(models.Model):
    name = models.CharField(max_length=200, unique=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_clear = models.DateTimeField(null=True, blank=True)
    user = models.CharField(max_length=50)
    category_id = models.ForeignKey('Categories', on_delete=models.PROTECT, default=1)

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_word', kwargs={'word_id': self.pk})


class UserDictionaries(models.Model):
    user = models.CharField(max_length=50)
    dictionary_id = models.ForeignKey('Dictionaries', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Словарь пользователя'
        verbose_name_plural = 'Словари пользователя'

    def __str__(self):
        return self.user

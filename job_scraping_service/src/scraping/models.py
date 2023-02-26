from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='City name',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)
    
    class Meta:
        verbose_name='City name'
        verbose_name_plural='City names'

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Programming language',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Programming language'
        verbose_name_plural = 'Programming languages'

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=250, verbose_name='')
    company = models.CharField(max_length=250, verbose_name='')
    description = models.TextField(verbose_name='')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='')
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 verbose_name='')

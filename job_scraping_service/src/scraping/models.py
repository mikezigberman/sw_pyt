from django.db import models
from django.utils.text import slugify

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='City name',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)
    
    class Meta:
        verbose_name='City name'
        verbose_name_plural='City names'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Job Title')
    company = models.CharField(max_length=250, verbose_name='Company')
    description = models.TextField(verbose_name='Vacancy description')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='City')
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 verbose_name='Programming language')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Job vacancy'
        verbose_name_plural = 'Jobs'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Vacancy, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
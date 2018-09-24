from django.db import models

# Create your models here.


class Toy(models.Model):
    name = models.CharField(max_length=64, blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=64, blank=True, default='')
    toy_category = models.CharField(max_length=64, blank=True, default='')
    release_date = models.DateTimeField()

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return f"{self.name} - category: {self.toy_category}"



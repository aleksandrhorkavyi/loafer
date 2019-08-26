from django.db import models
from django.shortcuts import reverse

class Phrase(models.Model):
    original = models.CharField(max_length=255, unique=True)
    translation = models.CharField(max_length=255)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    is_passed = models.BooleanField(default=False)
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position', 'date_create']

    def __str__(self):
        return self.original

    def get_absolute_url(self):
        return reverse('dict_url')

    def get_delete_url(self):
        return reverse('delete_phrase_url', kwargs={'id': self.pk})

    def get_update_url(self):
        return reverse('update_phrase_url', kwargs={'id': self.pk})

    def get_success_url(self):
        return reverse('success_phrase_url', kwargs={'id': self.pk})

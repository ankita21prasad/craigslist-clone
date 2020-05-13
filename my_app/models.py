from django.db import models


class Search(models.Model):
    search = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.search

    class Meta:
        verbose_name_plural = 'searches'
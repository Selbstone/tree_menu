from django.db import models
from django.urls import reverse

# Create your models here.

class MenuItem(models.Model):
    name_item = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True)
    named_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name_item

    def get_children(self):
        return self.menuitem_set.all()

    def get_url(self):
        if self.named_url:
            url_split = self.named_url.split()
            url = reverse(url_split[0], args=url_split[1:len(url_split)])
        elif self.url:
            url = self.url
        else:
            url = '/'

        return url
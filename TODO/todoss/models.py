from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Notes_model(models.Model):
    note = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse("note_delete", args=[self.id])
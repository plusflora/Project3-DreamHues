from django.db import models
from django.urls import reverse
from django import forms
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
FEELING = (
  # for a dropdown menu in regards to feeling of dream
  ('G', 'Good'),
  ('O', 'Okay'),
  ('N', 'Not Good'),
  ('B', 'Bad'),
)

TYPE = (
  ('N', 'Nightmare'),
  ('A', 'Amazing'),
  ('W', 'Weird')
)

class Palette(models.Model):
  # Assuming colors are in HEX format
  color1 = models.CharField(max_length=7)  
  color2 = models.CharField(max_length=7)
  color3 = models.CharField(max_length=7)
  color4 = models.CharField(max_length=7)
  color5 = models.CharField(max_length=7)

  def __str__(self):
    return f'{self.color1}, {self.color2}, {self.color3}, {self.color4}, {self.color5}'

class Dream(models.Model):
  date = models.DateField('Date of Dream')
  name = models.CharField(max_length=100)
  about = models.TextField(max_length=500)
  feeling = models.CharField(
    max_length=1,
    choices=FEELING,
    default=FEELING[0][0]
  )
  dream_type = models.CharField(
    max_length=1,
    choices=TYPE,
    default=TYPE[0][1]
  )
  dream_palette = Palette

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'dream_id': self.id})
  
  # class Meta:
  #   ordering = ['-date']

class DreamForm(forms.ModelForm):
  class Meta:
    model = Dream
    fields = ['date', 'name', 'about', 'feeling', 'dream_type']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  dream = models.ForeignKey(Dream, on_delete=models.CASCADE)

  def __str__(self):
    return f"dream_id: {self.dream_id} @{self.url}"
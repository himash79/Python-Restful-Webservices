from django.db.models import fields
from rest_framework import serializers
from django.db import models


# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    image = models.ImageField(upload_to='resources')
    status = models.BooleanField(default=False)


class SerializeClass(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'image', 'status')

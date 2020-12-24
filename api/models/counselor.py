from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Counselor(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
#  ripe = models.BooleanField()
  location = models.CharField(max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The counselor named '{self.name}' is located in {self.location}."
    # It is {self.ripe} that it is ripe."

  def as_dict(self):
    """Returns dictionary version of Counselor models"""
    return {
        'id': self.id,
        'name': self.name,
      #  'ripe': self.ripe,
        'location': self.location
    }

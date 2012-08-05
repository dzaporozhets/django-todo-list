from django.db import models

class Task(models.Model):
  title = models.CharField(max_length=255)
  pub_date = models.DateTimeField('date published')

  def __unicode__(self):
    return self.title

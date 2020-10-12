from django.db import models
from datetime import date, datetime

class instructor(models.Model):
    name = models.CharField(max_length=200, null=True)
    rate = models.FloatField(null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return 'Instructor: {0}'.format(self.name)

class client(models.Model):

    name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=15, null=True)
    female = models.BooleanField(default=True, null=True, blank=True)
    comments = models.TextField(max_length=200, null=True, blank=True)
    registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.registered)

class sale(models.Model):

    PTYPE = (
        ('Card', 'Card'),
        ('Bank', 'Bank'),
        ('Cash', 'Cash')

    )
    name = models.ForeignKey(client, null=True, on_delete=models.SET_NULL)
    sessions = models.IntegerField(null=True)
    paid = models.FloatField(null=True)
    payment_type = models.CharField(default='Card', max_length=100, null=True, choices=PTYPE)
    payment_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    comments = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.payment_date)

    @property
    def per_lesson(self):
        perprice = self.paid / int(self.sessions)
        return perprice

class lesson(models.Model):
    name = models.ForeignKey(client, null=True, on_delete=models.SET_NULL)
    lesson_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    instructedby = models.ForeignKey(instructor, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.name.name, self.lesson_date, self.instructedby)

class word(models.Model):
    vocab = models.CharField(max_length=200, null=True)
    meaning = models.CharField(max_length=200, null=True)
    frequency = models.IntegerField(null=True)

    def __str__(self):
        return '{0}'.format(self.vocab)

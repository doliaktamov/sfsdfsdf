from django.db import models
from datetime import date
from django.urls import reverse

class AbstractHuman(models.Model):
    fullname = models.CharField(max_length=50)
    birth_date = models.DateField()

    def get_age(self):
        age = date.today().year - self.birth_date.year
        return age

class Worker(AbstractHuman):
    work_position = models.CharField(max_length=50)
    work_experience = models.DateField()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('worker', kwargs={'pk': self.id, 'fullname': self.fullname} ) 


class Document(models.Model):
    inn = models.CharField(max_length=14)
    card_id = models.CharField(max_length=6)
    worker = models.OneToOneField(Worker, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        print(f'Сотрудник {self.worker.fullname} сохранен')
        return super().save(*args, **kwargs)



class Project(models.Model):
    worker = models.ManyToManyField(Worker, through='Membership')
    name = models.CharField(max_length=30)

class Membership(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Customer(AbstractHuman):
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)

class VIPCustomer(Customer):
    vip_status_start = models.DateField()
    donation_amount = models.CharField(max_length=999999)
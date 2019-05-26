from django.db import models


class client(models.Model):

    name = models.CharField(max_length=50)
    ovqat_1 = 'Mastava'
    ovqat_2 = 'shorva'
    ovqat_3 = 'chuchvara'
    ovqat = (
        (ovqat_1, 'mastava'),
        (ovqat_2, 'shorva'),
        (ovqat_3, 'chuchvara'),

    )
    birinchi_ovqatlar = models.CharField(choices=ovqat, max_length=12, null=True, blank=True)
    def __str__(self):
        return self.name
    
    ovqat_4='osh'
    ovqat_5='bishteks'
    ovqat_6='asortiment'

    ovqat2=(
        (ovqat_4,'osh'),
        (ovqat_5,'bishteks'),
        (ovqat_6,'asortiment')
    )

    ikkinchi_ovqatlar=models.CharField(choices=ovqat2,max_length=12,null=True,blank=True)


    ichimlik_1 = 'Pepsi'
    ichimlik_2 = 'Coca Cola'
    ichimlik_3 = 'kofe'
    ichimlik = (
        (ichimlik_1,'Pepsi'),
        (ichimlik_2,'Coca Cola'),
        (ichimlik_3,'kofe')

    )
    ichimlik = models.CharField(
        choices=ichimlik, max_length=12, null=True, blank=True)

class ofitsiant(models.Model):
    zakaz=models.ManyToManyField(client)
class oshpaz(models.Model):
    zakazlar=models.ManyToManyField(client)
    

class kassa(models.Model):
    hisob=models.ManyToManyField(client)
   
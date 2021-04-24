from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True, autoincrement=True)
    Name = models.CharField("Nome", max_length=100)
    RG = models.IntegerField()
    cpf = models.IntegerField()
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=3, choices=[
        ("Male", "Masculino"),
        ("Female", "Feminino"),
        ("Others", "outros"),
    ])


class Telephone(models.Model):
    id = models.AutoField(primary_key=True, autoincrement=True)
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    ddd = models.IntegerField()
    number = models.IntegerField()
    number_type = models.CharField(max_length=3, choices=[
        ("Cellphone", "Celular"),
        ("Home_Phone", "Residêncial"),
        ("commercial telephone", "Comercial"),
    ])

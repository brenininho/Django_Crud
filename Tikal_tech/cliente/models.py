from django.db import models
from dotenv import load_dotenv
load_dotenv()


class Client(models.Model):
    name = models.CharField("Nome", max_length=100)
    rg = models.IntegerField(null=False)
    cpf = models.IntegerField(null=False)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=30, choices=[
        ("Male", "Masculino"),
        ("Female", "Feminino"),
        ("Others", "outros"),
    ])


class Email(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)


class Telephone(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    ddd = models.IntegerField(max_length=3)
    number = models.IntegerField(max_length=9)
    number_type = models.CharField(max_length=30, choices=[
        ("cellphone", "Celular"),
        ("home_phone", "Residêncial"),
        ("commercial_telephone", "Comercial"),
    ])

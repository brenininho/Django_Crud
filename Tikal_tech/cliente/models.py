from django.db import models
import uuid
from dotenv import load_dotenv
load_dotenv()


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField("Nome", max_length=100)
    RG = models.IntegerField()
    cpf = models.IntegerField()
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=3, choices=[
        ("Male", "Masculino"),
        ("Female", "Feminino"),
        ("Others", "outros"),
    ])


class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)


class Telephone(models.Model):
    id = models.AutoField(primary_key=True, default=uuid.uuid4, editable=False)
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    ddd = models.IntegerField()
    number = models.IntegerField()
    number_type = models.CharField(max_length=3, choices=[
        ("Cellphone", "Celular"),
        ("Home_Phone", "Residêncial"),
        ("commercial telephone", "Comercial"),
    ])

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #id = models.ForeignKey(Question, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    votes = models.IntegerField(default=0)


from django.db import models


from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

COMPANY_CHOICES = (
    ("R", "RealStar"),
    ("E", "ElectroCo"),
    ("P", "Papsi"),
)

class Client(models.Model):
    name = models.CharField(max_length=120)
    company = models.CharField(max_length=1, choices=COMPANY_CHOICES)
    email = models.EmailField()


class Task(models.Model):
    text = models.TextField(blank=False, verbose_name='Текст',
                            help_text='Введите текст')
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               blank=True, null=True,
                               related_name="posts")


    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:15]




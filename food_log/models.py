from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User

# Create your models here.




class Calorie(models.Model):

    title = models.CharField(max_length=200,null=True)
    calories=models.FloatField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    MEAL_CHOICES=[
        ("breakfast","breakfast"),
        ("lunch","lunch"),
        ("dinner","dinner"),
    ]
    meal_type=models.CharField(max_length=120,choices=MEAL_CHOICES,default="lunch")
    bill_image=models.ImageField(upload_to="bills",null=True)#before apply makemigrations pip install pillow
    quantity=models.CharField(max_length=15)

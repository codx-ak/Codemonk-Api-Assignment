from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class Books(models.Model):
    class Category(models.TextChoices):
        Education = "Edcation", "Edcation"
        Mystery = "Mystery", "Mystery"
        Horror = "Horror", "Horror"
        Romance = "Romance", "Romance"
        Biography = "Biography", "Biography"
        Adventure = "Adventure", "Adventure"
        Novels_or_Comics = "Novels/Comics", "Novels/Comics"

    class Languages(models.TextChoices):
        Tamil = "Tamil", "Tamil"
        English = "English", "English"
        Hindi = "Hindi", "Hindi"
        Malayalam = "Malayalam", "Malayalam"
        Telugu = "Telugu", "Telugu"
        Kannada = "Kannada", "Kannada"

    title=models.CharField(max_length=150,null=False,blank=False)
    author=models.CharField(max_length=150,null=False,blank=False)
    category=models.CharField(choices=Category.choices,max_length=20,null=False,blank=False)
    language=models.CharField(choices=Languages.choices,max_length=20,null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    cover_image=models.ImageField(upload_to='images/',null=True,blank=True)
    book_file=models.FileField(upload_to='Files/',validators=[FileExtensionValidator(['pdf'])])
    publication_date=models.DateTimeField(null=False,blank=False)
    publisher=models.ForeignKey(User,on_delete=models.CASCADE)
    create_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

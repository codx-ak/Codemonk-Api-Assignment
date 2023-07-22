# Generated by Django 4.2.3 on 2023-07-22 11:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('category', models.CharField(choices=[('Edcation', 'Edcation'), ('Mystery', 'Mystery'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Biography', 'Biography'), ('Adventure', 'Adventure'), ('Novels/Comics', 'Novels/Comics')], max_length=20)),
                ('language', models.CharField(choices=[('Tamil', 'Tamil'), ('English', 'English'), ('Hindi', 'Hindi'), ('Malayalam', 'Malayalam'), ('Telugu', 'Telugu'), ('Kannada', 'Kannada')], max_length=20)),
                ('description', models.TextField(max_length=500)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('book_file', models.FileField(upload_to='Files/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('publication_date', models.DateTimeField()),
                ('create_on', models.DateTimeField(auto_now_add=True)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 4.2.11 on 2024-03-17 09:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_create_category'),
        ('authors', '0002_create_author'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('^[a-zA-Z\\s]*$', 'The name should contain only letters!')])),
                ('book_image', models.ImageField(upload_to='books/')),
                ('description', models.TextField()),
                ('serial', models.CharField(editable=False, max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='authors.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
        ),
    ]

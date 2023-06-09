# Generated by Django 4.1.7 on 2023-03-21 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yazi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=120)),
                ('yazar', models.CharField(blank=True, max_length=150, null=True)),
                ('metin', models.TextField()),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(editable=False, max_length=130, unique=True)),
                ('goruntulenme', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Yorum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metin', models.TextField()),
                ('yayinTarihi', models.DateTimeField(auto_now_add=True)),
                ('yazi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='yazi.yazi')),
            ],
        ),
    ]

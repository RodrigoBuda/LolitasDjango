# Generated by Django 4.2 on 2023-05-10 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLolitas', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='servicios/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
            },
        ),
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]

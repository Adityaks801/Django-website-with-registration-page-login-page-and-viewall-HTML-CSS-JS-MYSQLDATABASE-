# Generated by Django 5.0.6 on 2024-07-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("eid", models.CharField(max_length=20)),
                ("ename", models.CharField(max_length=100)),
                ("econtact", models.CharField(max_length=15)),
                ("eemail", models.EmailField(max_length=100)),
                ("eaddress", models.CharField(max_length=100)),
                ("egender", models.CharField(max_length=100)),
                ("edob", models.DateField(max_length=100)),
            ],
        ),
    ]

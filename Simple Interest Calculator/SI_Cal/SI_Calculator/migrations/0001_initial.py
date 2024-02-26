# Generated by Django 4.2.2 on 2024-02-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Calculation",
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
                ("principal", models.DecimalField(decimal_places=2, max_digits=10)),
                ("rate", models.DecimalField(decimal_places=2, max_digits=10)),
                ("time", models.IntegerField()),
                ("result", models.DecimalField(decimal_places=2, max_digits=10)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-20 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Imovel",
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
                ("ref", models.CharField(default="", max_length=7)),
                ("condominio", models.CharField(default="", max_length=200)),
                ("endereco", models.CharField(default="", max_length=200)),
                ("km", models.IntegerField(default=0)),
                ("valor_venda", models.FloatField(default=0)),
                ("valor_aluguel", models.FloatField(default=0)),
                ("valor_condominio", models.FloatField(default=0)),
                ("valor_iptu", models.FloatField(default=0)),
                ("ano_construcao", models.DateField()),
                ("ano_reforma", models.DateField()),
                ("zfile", models.FileField(default="", upload_to="uploads/")),
                ("nome", models.CharField(default="", max_length=50)),
                ("telefone", models.CharField(default="", max_length=11)),
                ("email", models.CharField(default="", max_length=200)),
                (
                    "observacoes",
                    models.CharField(blank=True, default="", max_length=400, null=True),
                ),
                ("tipo_interesse", models.CharField(default="", max_length=50)),
                ("regiao_interesse", models.CharField(default="", max_length=50)),
                ("uf_interesse", models.CharField(default="", max_length=2)),
                ("valor_minimo_interesse", models.IntegerField(default=0)),
                ("valor_maximo_interesse", models.IntegerField(default=0)),
                (
                    "corretor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

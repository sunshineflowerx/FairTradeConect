# Generated migration to remove 'gestor' and 'operador' from Perfil choices

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comerciojusto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='tipo',
            field=models.CharField(choices=[('produtor', 'Produtor'), ('empresa', 'Empresa')], max_length=20),
        ),
    ]

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='email',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='idade',
        ),
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='disponibilidade',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='produtos/'),
        ),
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]

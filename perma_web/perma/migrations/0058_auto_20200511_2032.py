# Generated by Django 2.2.12 on 2020-05-11 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perma', '0057_auto_20200504_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorship',
            name='registrar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sponsorships', to='perma.Registrar'),
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsorships', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='sponsorship',
            constraint=models.UniqueConstraint(fields=('registrar', 'user'), name='unique_sponsorship'),
        ),
    ]

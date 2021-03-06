# Generated by Django 3.1.4 on 2020-12-26 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0004_auto_20201222_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='displayName',
            field=models.CharField(default='Twitter User', max_length=50),
        ),
    ]

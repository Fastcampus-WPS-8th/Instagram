# Generated by Django 2.0.6 on 2018-06-29 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20180626_0524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(choices=[('f', 'Follow'), ('b', 'Block')], max_length=1)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_by_from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_by_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='relations',
            field=models.ManyToManyField(blank=True, through='members.Relation', to=settings.AUTH_USER_MODEL),
        ),
    ]

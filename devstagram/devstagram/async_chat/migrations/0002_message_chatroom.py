# Generated by Django 3.1.7 on 2021-03-17 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('async_chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='chatroom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='async_chat.chatroom'),
            preserve_default=False,
        ),
    ]
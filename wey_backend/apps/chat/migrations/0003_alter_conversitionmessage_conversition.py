# Generated by Django 4.2.2 on 2023-07-01 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_conversition_id_alter_conversitionmessage_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversitionmessage',
            name='conversition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.conversition'),
        ),
    ]
# Generated by Django 4.0.8 on 2023-01-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_alter_commande_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vente',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=100, null=True),
        ),
    ]

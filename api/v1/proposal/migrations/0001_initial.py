<<<<<<< HEAD
# Generated by Django 4.2.2 on 2023-07-03 05:16
=======
# Generated by Django 4.2.2 on 2023-07-03 05:06
>>>>>>> cb315bb (Server push)

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'new'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='new', max_length=8)),
            ],
        ),
    ]

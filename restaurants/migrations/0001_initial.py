# Generated by Django 4.0.4 on 2022-04-18 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('cuisine_type', models.CharField(choices=[('italian', 'Italian'), ('mexican', 'Mexican'), ('tex-mex', 'Tex-Mex'), ('chinese', 'Chinese'), ('thai', 'Thai'), ('japanese', 'Japanese'), ('american', 'American')], max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_type', models.CharField(choices=[('breakfast', 'Breakfast'), ('brunch', 'Brunch'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('happy hour', 'Happy Hour'), ('late night', 'Late Night')], max_length=200)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='restaurants.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='restaurants.menu')),
            ],
        ),
    ]

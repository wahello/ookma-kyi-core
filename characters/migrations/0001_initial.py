# Generated by Django 2.2.9 on 2020-01-22 16:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Belt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Belt name', max_length=32)),
                ('belt_image', models.ImageField(upload_to='belts/')),
                ('min_xp', models.PositiveIntegerField(help_text='Minimum xp required to obtain belt, 0 for first belt', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999999)])),
                ('max_xp', models.PositiveIntegerField(help_text='Maximum xp for belt', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999999)])),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name for your character. Warning this cannot be changed latter!', max_length=32)),
                ('xp', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999999)])),
                ('wins', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999999)])),
                ('loses', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999999)])),
                ('draws', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999999)])),
                ('belt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.Belt')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

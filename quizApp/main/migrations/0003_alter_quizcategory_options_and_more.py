# Generated by Django 4.1.5 on 2023-02-09 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_quizquestions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizcategory',
            options={'verbose_name_plural': 'Quiz Categories'},
        ),
        migrations.AlterModelOptions(
            name='quizquestions',
            options={'verbose_name_plural': 'Quiz Questions'},
        ),
        migrations.CreateModel(
            name='userSubmittedAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_answer', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.quizquestions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Users Submitted Answers',
            },
        ),
    ]

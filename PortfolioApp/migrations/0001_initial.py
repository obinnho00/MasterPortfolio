# Generated by Django 5.1.4 on 2024-12-14 15:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.TextField()),
                ('fun_interests', models.TextField()),
            ],
            options={
                'db_table': 'about_me',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='cv_files/')),
            ],
            options={
                'db_table': 'cv',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=100)),
                ('field_of_study', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('gpa', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'education',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'personal_information',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('technologies_used', models.TextField(blank=True, null=True)),
                ('project_url', models.URLField(blank=True, null=True)),
                ('repository_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'projects',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=150, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='references_pictures/')),
            ],
            options={
                'db_table': 'references_table',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('proficiency', models.IntegerField(default=0)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='skill_pictures/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'skills',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WebsitePolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_of_use', models.TextField()),
                ('policy_statement', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'website_policy',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TechnicalSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Libraries and Frameworks', 'Libraries and Frameworks'), ('Data Science & Analysis', 'Data Science & Analysis'), ('Programming Languages', 'Programming Languages'), ('Backend Development', 'Backend Development'), ('Frontend Development', 'Frontend Development'), ('Version Control & Tools', 'Version Control & Tools'), ('Development Practices', 'Development Practices'), ('Other', 'Other')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('skill_level', models.PositiveIntegerField(default=5, help_text='Skill level on a scale of 1 to 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'technical_skill',
                'managed': True,
                'unique_together': {('category', 'name')},
            },
        ),
    ]

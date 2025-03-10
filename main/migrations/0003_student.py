# Generated by Django 4.2.10 on 2024-04-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('fname', models.CharField(max_length=100)),
                ('email', models.EmailField(default='example@example.com', max_length=254)),
                ('phone_num', models.IntegerField(default='xxx-xxx-xxxx')),
                ('dob', models.DateField(default='DD-MM-YYYY')),
                ('student_id', models.CharField(default='xxxxxxx', max_length=50, primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='Other', max_length=1)),
                ('Str_add', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(default='Brownsville', max_length=50)),
                ('postal_code', models.IntegerField(default='785xx')),
                ('state', models.CharField(default='Texas', max_length=50)),
                ('question1', models.CharField(choices=[('E', 'Elementary'), ('J', 'Jr. High School/Middle School'), ('H', 'High School'), ('S', 'Some College'), ('C', 'College Degree'), ('U', 'Unknown')], max_length=1)),
                ('question2', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('question3', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('question4', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('GPA', models.DecimalField(decimal_places=2, max_digits=4)),
                ('question6', models.CharField(choices=[('C', 'Plan on going to college'), ('N', 'Not going to college'), ('M', 'Plan to enroll in military'), ('W', 'Plan to work'), ('O', 'Other')], max_length=1)),
                ('first_choice', models.CharField(max_length=200)),
                ('second_choice', models.CharField(max_length=200)),
                ('question9', models.CharField(choices=[('C', 'Certificate'), ('A', 'Associate'), ('B', 'Bachelors'), ('M', 'Military'), ('O', 'Other')], max_length=1)),
                ('question10', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('question11', models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted')], max_length=1)),
                ('question12', models.CharField(choices=[('N', 'Not Testing'), ('R', 'Registered'), ('T', 'Tested')], max_length=1)),
                ('question13', models.CharField(choices=[('S', 'SAT'), ('A', 'ACT'), ('N', 'N/A')], max_length=1)),
                ('test_date', models.DateField()),
                ('question15', models.CharField(choices=[('S', 'Sent'), ('P', 'Pending')], max_length=1)),
                ('question16', models.CharField(choices=[('S', 'Sent'), ('P', 'Pending')], max_length=1)),
                ('question17', models.CharField(choices=[('T', 'Tested-Pass'), ('F', 'Tested-Fail'), ('P', 'Pending')], max_length=1)),
                ('question18', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('question19', models.CharField(choices=[('F', 'FAFSA'), ('T', 'TAFSA'), ('O', 'Other')], max_length=1)),
                ('question20', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('appliedforAid', models.DateField()),
            ],
        ),
    ]

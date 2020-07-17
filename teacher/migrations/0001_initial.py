# Generated by Django 3.0.5 on 2020-07-04 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('administration', '0001_initial'),
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village', models.TextField()),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='address.District')),
                ('union', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='address.Union')),
                ('upazilla', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='address.Upazilla')),
            ],
        ),
        migrations.CreateModel(
            name='EducationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_exam', models.CharField(max_length=100)),
                ('institute', models.CharField(max_length=255)),
                ('group', models.CharField(max_length=255)),
                ('board', models.CharField(max_length=255)),
                ('passing_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=45)),
                ('trainer', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('science', 'Science'), ('business', 'Business'), ('huanities', 'Humanities')], max_length=20)),
                ('joning_date', models.DateField()),
                ('institute_name', models.CharField(max_length=100)),
                ('scale', models.IntegerField()),
                ('grade_of_post', models.CharField(max_length=45)),
                ('first_time_scale_due_year', models.IntegerField()),
                ('second_time_scale_due_year', models.IntegerField()),
                ('promotion_due_year', models.IntegerField()),
                ('recreation_leave_due_year', models.IntegerField()),
                ('expected_retirement_year', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.Department')),
                ('job_designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Designation')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('place', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('photo', models.ImageField(upload_to='')),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=45)),
                ('nationality', models.CharField(choices=[('Bangladeshi', 'Bangladeshi'), ('Others', 'Others')], max_length=45)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Hinduism', 'Hinduism'), ('Buddhism', 'Buddhism'), ('Christianity', 'Christianity'), ('Others', 'Others')], max_length=45)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('blood_group', models.CharField(choices=[('a+', 'A+'), ('o+', 'O+'), ('b+', 'B+'), ('ab+', 'AB+'), ('a-', 'A-'), ('o-', 'O-'), ('b-', 'B-'), ('ab-', 'AB-')], max_length=5)),
                ('e_tin', models.IntegerField(unique=True)),
                ('nid', models.IntegerField(unique=True)),
                ('driving_license_passport', models.IntegerField(unique=True)),
                ('phone_no', models.CharField(max_length=11, unique=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('father_name', models.CharField(max_length=45)),
                ('mother_name', models.CharField(max_length=45)),
                ('marital_status', models.CharField(choices=[('married', 'Married'), ('widowed', 'Widowed'), ('separated', 'Separated'), ('divorced', 'Divorced'), ('single', 'Single')], max_length=10)),
                ('is_delete', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.AddressInfo')),
                ('education', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.EducationInfo')),
                ('experience', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.ExperienceInfo')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.JobInfo')),
                ('training', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.TrainingInfo')),
            ],
        ),
    ]

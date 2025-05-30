# Generated by Django 4.2.2 on 2023-07-02 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('is_free', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Participant_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='speakers/')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('linkedin_link', models.URLField(blank=True)),
                ('twitter_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('topic', models.CharField(max_length=150)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_app.event_management')),
                ('speaker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_app.speaker_management')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=8)),
                ('payment_method', models.CharField(max_length=50)),
                ('payment_date', models.DateField()),
                ('transaction_id', models.CharField(max_length=100)),
                ('payment_status', models.CharField(choices=[('PAID', 'Paid'), ('PENDING', 'Pending'), ('FAILED', 'Failed')], max_length=10)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_app.event_management')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_app.participant_management')),
            ],
        ),
    ]

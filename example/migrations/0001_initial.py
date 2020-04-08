# Generated by Django 3.0.4 on 2020-04-08 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_extra_referrals', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.PositiveIntegerField(blank=True, editable=False, null=True, verbose_name='Reg number')),
                ('inner_id', models.CharField(blank=True, editable=False, max_length=50, null=True, unique=True, verbose_name='Inner ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('is_paid', models.BooleanField(default=False, editable=False)),
                ('is_cancelled', models.BooleanField(default=False, editable=False)),
                ('fullname', models.CharField(max_length=150)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('referral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_extra_referrals.Referral')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.PositiveIntegerField(blank=True, editable=False, null=True, verbose_name='Reg number')),
                ('inner_id', models.CharField(blank=True, editable=False, max_length=50, null=True, unique=True, verbose_name='Inner ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('is_paid', models.BooleanField(default=False, editable=False)),
                ('is_cancelled', models.BooleanField(default=False, editable=False)),
                ('fullname', models.CharField(max_length=150)),
                ('campaigner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donation_campaigns', to='django_extra_referrals.Referral')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('referral', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donation_referrals', to='django_extra_referrals.Referral')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
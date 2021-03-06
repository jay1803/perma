# Generated by Django 2.2.10 on 2020-02-20 20:58

from django.db import migrations

import logging
logger = logging.getLogger(__name__)

def ignore_failed_ia_uploads(apps, schema_editor):
    Link = apps.get_model('perma', 'Link')
    updated = Link.objects.filter(
        internet_archive_upload_status='failed_permanently'
    ).update(
        internet_archive_upload_status='not_started'
    )
    logger.info(f"Updated {updated} Links")

class Migration(migrations.Migration):

    dependencies = [
        ('perma', '0050_auto_20200220_2057'),
    ]

    operations = [
        migrations.RunPython(ignore_failed_ia_uploads, migrations.RunPython.noop),
    ]

# Generated by Django 4.1.1 on 2022-10-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_delete_instructor_course_about_tutor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tutor_facebook_profile_link',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='tutor_google_profile_link',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='tutor_instagram_profile_link',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='tutor_twitter_profile_link',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]

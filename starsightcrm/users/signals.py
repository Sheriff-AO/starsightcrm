from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db.models import signals
from .models import Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Profile created")


post_save.connect(create_profile, sender=User)


def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    print("Profile saved")


post_save.connect(save_profile, sender=User)


def delete_user(sender, instance=None, **kwargs):
    try:
        instance.user
    except User.DoesNotExist:
        pass
    else:
        instance.user.delete()


signals.post_delete.connect(delete_user, sender=Profile)

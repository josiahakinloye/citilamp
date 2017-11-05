import  datetime

from django.db import models

from django.utils import timezone
# Create your models here.
class AdOwner(models.Model):
    name = models.CharField(primary_key=True,unique=True)
    #todo:addreess is required how to make sure model fileds are not empty
    address  = models.TextField()

class Ads(models.Model):
    title = models.CharField(max_length=250,primary_key=True)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now())
    stop_date = models.DateTimeField()
    def is_valid(self):
        """
        This checks if a particular ad is valid.So admins can no when to take out an ad
        :return: Bool
        """
        now = timezone.now()
        return now < self.stop_date

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.stop_date < self.start_date:
            self.save()
        else:
            raise ads_error("Stop date is less than start date")


class ads_error(Exception):
    pass
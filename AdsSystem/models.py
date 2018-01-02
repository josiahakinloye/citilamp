from datetime import date

from django.db import models



class AdsError(Exception):
    """
    Exception class for Anything relating to ads
    """
    pass

class Ads(models.Model):
    """
    Ads model
    """
    title = models.CharField(max_length=250)
    description = models.TextField()

    # for the duration of ad
    start_date = models.DateField(default=date.today)
    stop_date = models.DateField()

    #owner(the poster) of ad details
    owner_name = models.CharField(max_length=999,verbose_name="owner of ad")
    owner_phone_number = models.IntegerField()
    owner_email = models.EmailField()

    #is the ad approved is changed to true , has to be changed to true in admin panel
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural =  'AdS'

    def has_expired(self):
        """
        This checks if a particular has expired.So admins can know when to take out an ad
        :return: Bool
        """
        return date.today() >= self.stop_date

    has_expired.admin_order_field = 'stop_date'
    has_expired.boolean = True
    has_expired.short_description = "Has Ad expired?"

    def save(self, *args, **kwargs):
        #Ensure start date is not less than today and stop date is greater than start date
        if date.today() <= self.start_date and self.stop_date > self.start_date:
            super(Ads, self).save(*args, **kwargs)
        else:
            raise AdsError("Ensure start date is not less than today and stop date is greater than start date")

    def __str__(self):
        return self.title + " by "+ self.owner_name


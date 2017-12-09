import datetime
import math
import random
import re
import string

from django.utils.html import strip_tags
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def count_words(html_string):
    words = strip_tags(html_string)
    matching_words = re.findall(r'\w+', words)
    count = len(matching_words)
    return count

def get_read_time(html_string):
    count = count_words(html_string)
    read_time_min = math.ceil(count/200.0) # assuming a reading speed of 200 words per minute
    read_time = str(datetime.timedelta(minutes=read_time_min))
    return read_time
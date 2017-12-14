import math
import random
import re
import string

from django.utils.html import strip_tags
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    Generate a unique slug for each instance of a class, if slug already exits
    create a new slug
    :param instance: class instance
    :param new_slug: slug to saved to instance
    :return: str
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def count_words(html_string):
    """
    Count the number of words in a string
    :param html_string: string to be counted
    :return: int number of words
    """
    words = strip_tags(html_string)
    matching_words = re.findall(r'\w+', words)
    count = len(matching_words)
    return count


def get_read_time(html_string):
    """
    Get time required to read a text
    :param html_string: string to be read
    :return: int estimated number of minutes required to read
    """
    count = count_words(html_string)
    reading_speed = 200.0  # assuming a reading speed of 200 words per minute
    read_time_min = math.ceil(count/reading_speed)
    return read_time_min

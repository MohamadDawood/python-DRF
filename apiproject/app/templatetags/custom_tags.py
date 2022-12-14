from django.shortcuts import render
from django.template.defaultfilters import register

from app.models import Job
from django import template



# register = template.Library()



@register.filter(name='lower')
def lower(value, arg): # Only one argument.
    """Converts a string into all lowercase"""
    # lower()
    return arg.upper()


# register.filter('lower', lower)
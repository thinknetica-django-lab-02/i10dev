from django import template
from time import gmtime, strftime

register = template.Library()

@register.simple_tag
def currenttime():
    return strftime("%H:%M:%S", gmtime())

@register.filter
def revers(val):
    return val[::-1]
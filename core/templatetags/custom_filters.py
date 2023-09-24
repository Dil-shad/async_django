from django import template

register = template.Library()

@register.filter
def swapcase(text):
    return text.swapcase()

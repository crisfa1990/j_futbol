from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_field(form, field_name):
    try:
        return form[field_name]
    except KeyError:
        return None

@register.filter
def add(value, arg):
    return str(value) + str(arg)
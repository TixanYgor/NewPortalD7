"""
Данный файл нужен для того, чтобы создавать и регистрировать собственные фильтры.
"""
from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    censor_list = ['мат']
    text = value.split()
    for word in text:
        if word.lower() in censor_list:
            value = value.replace(word, '[CENSORED]')
    return value


@register.filter(name='multiply')
def multiply(value, arg):
    if isinstance(value, str) and isinstance(arg, int):
        return str(value) * arg
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}')

from django.template import Library

register = Library()


@register.filter()
def odd(val):
    """判断是否为奇数"""
    return val % 2 == 1
#自定义过滤器和标签

from django import template
import datetime

register = template.Library()

#过滤器
@register.filter(name="cut")
def cut(value, arg):
    return value.replace(arg, '')

#标签
@register.simple_tag(name="current_time")
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.inclusion_tag("blog/results.html")
def show_results(forms):
    return {"forms": forms}
from django import template
register=template.Library()
@register.filter(name='cut')
def cutfun(value,arg):
    """
    This function cuts out all the value of"arg"from the string

    """
    return value.replace(arg, '')
#register.filter('cut',cutfun)
from django import template

register = template.Library()

@register.filter(name='hi')
def hi(value,arg):
    '''
    this cuts out all the values in the string
    '''
    return value.replace(arg,'')

# register.filter('cut',cut) instead of using this we can directly use decorators which we used in line 5

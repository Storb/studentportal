from django.core.urlresolvers import reverse
from django.template import Library

register = Library()

@register.simple_tag
def go_to_admin(obj):
    url = reverse('admin:{0}_{1}_change' .format(obj._meta.app_label,
                                                 obj._meta.model_name), args=(obj.id,))
    return url


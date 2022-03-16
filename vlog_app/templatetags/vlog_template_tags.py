from django import template
from vlog_app.models import Tag

register=template.Library()
@register.inclusion_tag('tags.html')
def get_tags_list(current_tag=None):
    return {'tags': Tag.objects.all(),'current_tag': current_tag}
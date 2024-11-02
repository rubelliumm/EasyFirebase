from django import template
from EasyFirebase.firebase import getUrl


register = template.Library()


@register.filter
def load_url_of(obj, field_name):
    try:
        uuid_list = obj.file_uuid[str(field_name)]
        return makeUrl(uuid_list)
    except Exception as e:
        raise ValueError(f"Unexpected data in file_uuid. Exception: {str(e)}")


def makeUrl(uuid_list):
    l = []
    for x in uuid_list:
        a = getUrl(x)
        l.append(a)
    return l

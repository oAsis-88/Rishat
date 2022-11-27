from django import template


register = template.Library()


class GetInfoItemsList(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        items: list = context.get("Items", [])
        context["list_items"] = items
        return ''


@register.tag(name='result_list_items')
def get_info_item(parser, token):
    args = token.split_contents()
    return GetInfoItemsList()


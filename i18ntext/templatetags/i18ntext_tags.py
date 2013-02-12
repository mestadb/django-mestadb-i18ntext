# -*- coding: utf-8 -*-

from django import template
from django.core import urlresolvers
from i18ntext.models import Text

register = template.Library()

@register.tag(name="i18n_text")
def get_i18ntext(parser, token):
    """
    Parse i18n_text tag's arguments.
    """
    try: # split_contents() knows not to split quoted strings.
        tag_name, key, placeholder = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires two arguments" % token.contents.split()[0])
    if not (key[0] == key[-1] and key[0] in ('"', "'")) or\
       not (placeholder[0] == placeholder[-1] and placeholder[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's arguments should be in quotes" % tag_name)
    key = key.strip('"').strip("'")
    placeholder = placeholder.strip('"').strip("'")
    return I18nText(key, placeholder)


class I18nText(template.Node):
    """
    Render i18n_text object. If object with key doesn't exist, it will be
    created. A new Text object will have active flag set to False.
    All objects with active == False will be rendered with a postfix link to
    object's admin page.
    """
    def __init__(self, key, placeholder):
        self.key = key
        self.placeholder = placeholder
    def render(self, context):
        try:
            text = Text.objects.get(key=self.key)
        except Text.DoesNotExist:
            text = Text(key=self.key, text=self.placeholder, active=False)
            text.save()
        t = text.text
        if text.active is False:
            change_url = urlresolvers.reverse('admin:i18ntext_text_change', args=(text.id,))
            t += ' <a href="%s" style="border:1px solid #ccc; background-color:#eee">Edit</a>' % change_url
        return t


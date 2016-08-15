from django import template
from ..models import Message, Quran

register = template.Library()


@register.inclusion_tag('account/latest_messages.html')
def show_latest_messages(count=5):
    latest_messages = Message.published.order_by('-publish')[:count]
    return {'latest_messages': latest_messages}


@register.inclusion_tag('account/latest_aye.html')
def show_latest_quran(count=5):
    latest_quran = Message.published.order_by('-publish')[:count]
    return {'latest_quran': latest_quran}
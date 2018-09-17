from django.urls import path
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    # redirect to inbox
    path(
    '',
    RedirectView.as_view(permanent=True, url='inbox/'),
    name='messages_redirect'
    ),
    # inbox
    path(
        'inbox/',
        views.inbox,
        name='messages_inbox'
        ),
    # outbox
    path(
        'outbox/',
        views.outbox,
        name='messages_outbox'
        ),
    # compose
    path(
        'compose/',
        views.compose,
        name='messages_compose'
        ),
    # compose to username from url
    path(
        'compose/<str:recipient>/',
        views.compose,
        name='messages_compose_to'
        ),
    # reply
    path(
        'reply/<slug:message_id>/',
        views.reply,
        name='messages_reply'
        ),
    # view
    path(
        'view/<slug:message_id>/',
        views.view,
        name='messages_detail'
        ),
    # delete
    path(
        'delete/<slug:message_id>/',
        views.delete,
        name='messages_delete'
        ),
    # undelete
    path(
        'undelete/<slug:message_id>/',
        views.undelete,
        name='messages_undelete'
        ),
    # trash
    path(
        'trash/',
        views.trash,
        name='messages_trash'
        ),
    ]
from .views import (question_list,
                    question_detail,
                    question_create,
                    question_update,
                    question_delete,
                    )
from django.conf.urls import include, url



urlpatterns = [

        url(r'questions/$', question_list, name='question-list'),
        url(r'questions/(?P<id>[0-9]+)/$', question_detail, name='question-detail'),
        url(r'questions/create/$', question_create, name='question-create'),
        url(r'questions/(?P<id>[0-9]+)/update/$', question_update, name='question-update'),
        url(r'questions/(?P<id>[0-9]+)/delete/$', question_delete, name='question-delete'),

]

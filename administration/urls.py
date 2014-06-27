from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required as lr
from forum.views import AdminCourseForumView
from views import AdminView

urlpatterns = patterns(
    '',
    # list all courses
    url(r'^$', lr(RedirectView.as_view(url="courses/")), name="administration.home"),
    url(r'^courses/$', AdminView.as_view(template_name="courses_admin.html")),

    # create and edit course
    url(r'^courses/new/$', AdminView.as_view(template_name="new_course.html")),
    url(r'^courses/(?P<pk>[1-9][0-9]*)/$', AdminView.as_view(template_name="new_course.html")),

    # create and edit lesson
    url(r'^courses/(?P<course_id>[1-9][0-9]*)/lessons/new/$', AdminView.as_view(template_name="new_lesson.html")),
    url(r'^courses/(?P<course_id>[1-9][0-9]*)/lessons/(?P<pk>[1-9][0-9]*)/$', AdminView.as_view(template_name="new_lesson.html")),

    # create and edit portfolio
    url(r'^courses/(?P<course_id>[1-9][0-9]*)/portfolios/new/$', AdminView.as_view(template_name="new_portfolio_question.html")),
    url(r'^courses/(?P<course_id>[1-9][0-9]*)/portfolios/(?P<pk>[1-9][0-9]*)/$', AdminView.as_view(template_name="new_portfolio_question.html")),

    # messages
    url(r'^course/(?P<course_id>[1-9][0-9]*)/messages/$', AdminView.as_view(template_name="messages.html")),
    url(r'^course/(?P<course_id>[1-9][0-9]*)/message/(?P<message_id>[1-9][0-9]*)$', AdminView.as_view(template_name="message.html")),

    url(r'^course/(?P<course_id>[1-9][0-9]*)/forum/', AdminCourseForumView.as_view()),

    url(r'^users/$', AdminView.as_view(template_name="users.html")),

    url(r'^course/(?P<course_id>[1-9][0-9]*)/stats/$', AdminView.as_view(template_name="stats.html")),

)

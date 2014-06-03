__author__ = 'dali'
from django.db import models
from jsonfield import JSONField
from accounts.models import TimtecUser
from core.models import Course
from django.utils.translation import ugettext_lazy as _


class PortfolioQuestion(models.Model):
    course = models.ForeignKey(Course, related_name='portfolio_questions', verbose_name=_('Course'))
    description = models.TextField(_('Description'))
    timestamp = models.DateTimeField(_('Date'), auto_now_add=True)
    type = models.CharField(_('Type'), max_length=255)

class PortfolioAnswer(models.Model):
    portfolio_question = models.ForeignKey(PortfolioQuestion, verbose_name=_('Portfolio Question'))
    user = models.ForeignKey(TimtecUser, verbose_name=_('Student'))
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    given = JSONField(_('Given answer'))
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'))



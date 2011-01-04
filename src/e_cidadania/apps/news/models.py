# -*- coding: utf-8 -*-
#
# Copyright (c) 2010 Cidadanía Coop.
# Written by: Oscar Carballal Prego <info@oscarcp.com>
#
# This file is part of e-cidadania.
#
# e-cidadania is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# e-cidadania is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with e-cidadania. If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from tagging.fields import TagField
from tagging.models import Tag

class Post(models.Model):
    
    """
    Model of a news post.
    """
    post_title = models.CharField(_('Title'), max_length=100)
    post_message = models.TextField(_('Text'))
    post_pubdate = models.DateTimeField(_('Date'), auto_now_add=True)
    post_lastup = models.DateTimeField(_('Last update'), auto_now=True)
    post_author = models.ForeignKey(User, verbose_name=_('Author'))

    def save(self, *args, **kwargs):
        self.post_author = User.username

    def __unicode__(self):
        return self.post_title

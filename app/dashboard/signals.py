# -*- coding: utf-8 -*-
"""Handle dashboard related signals.

Copyright (C) 2018 Gitcoin Core

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
import logging

from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .notifications import maybe_market_to_github

logger = logging.getLogger(__name__)


def m2m_changed_interested(sender, instance, action, reverse, model, **kwargs):
    """Handle changes to Bounty interests."""
    profile_handles = []

    for profile in instance.interested.select_related('profile').all().order_by('pk'):
        profile_handles.append((profile.profile.handle, profile.profile.absolute_url))

    if action in ['post_add', 'post_remove']:
        maybe_market_to_github(instance, 'work_started',
                               interested=profile_handles)

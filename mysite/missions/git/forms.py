# This file is part of OpenHatch.
# Copyright (C) 2010 Jack Grigg
# Copyright (C) 2010 John Stumpo
# Copyright (C) 2010, 2011 OpenHatch, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import django.forms

class CheckoutForm(django.forms.Form):
    secret_word = django.forms.CharField(error_messages={'required': 'No author was given.'})

class DiffForm(django.forms.Form):
    diff = django.forms.CharField(error_messages={'required': 'No git diff output was given.'}, widget=django.forms.Textarea())

class RebaseForm(django.forms.Form):
    secret_word = django.forms.CharField(error_messages={'required': 'The password was incorrect.'})
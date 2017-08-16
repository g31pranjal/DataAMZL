# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Blocks,Station

# Register your models here.

admin.site.register(Station)
admin.site.register(Blocks)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blocks(models.Model):
    block=models.CharField(max_length=16)
    block_station=models.CharField(max_length=4)
    
class Station(models.Model):
    station=models.ForeignKey(Blocks,on_delete=models.CASCADE)
    

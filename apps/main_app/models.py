from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User
import datetime
import re
from dateutil import parser

# Create your models here.
class TravelManager(models.Manager):
    def validator(self, postData):
        pass
        # results = {'status': True, 'errors': []}
        # if len(postData['destination']) < 1:
        #     results['errors'].append('Destination too short')
        #     results['status'] = False
        # if len(postData['desc']) < 1:
        #     results['errors'].append('Description too short')
        #     results['status'] = False
        
        # formDateFrom = parser.parse(postData['dateFrom'])
        # formDateTo = parser.parse(postData['dateTo'])
        # if not len(postData['dateFrom']):
        #     results['errors'].append('Travel Date From must contain a date')
        #     results['status'] = False
        # if not len(postData['dateTo']):
        #     results['errors'].append('Travel Date To must contain a date')
        #     results['status'] = False
        
        # if not formDateFrom < datetime.now():
        #     results['errors'].append('Travel Date must be in future')
        #     results['status'] = False

        # if not formDateTo < datetime.now():
        #     results['errors'].append('Travel Date must be in future')
        #     results['status'] = False

        # if formDateTo < formDateFrom:
        #     results['errors'].append("You can't start a trip after it ends")
        #     results['status'] = False
        # return results
    
class Travel(models.Model):
    destination = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    dateFrom = models.DateField(auto_now=False, auto_now_add=False)
    dateTo = models.DateField(auto_now=False, auto_now_add=False)
    user = models.ManyToManyField(User, related_name="travel")
    tripOrginizer = models.CharField(max_length=200)
    objects = TravelManager()
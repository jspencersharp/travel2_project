from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
from dateutil import parser
from datetime import datetime

# Create your models here.

class UserManager(models.Manager):
    def loginVal(self, postData):
        results = {'status': True, 'errors': [], 'user': None}
        users = self.filter(email = postData['email'])
        if len(users) < 1:
            results['status'] == False
        else: 
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
                results['user'] = users[0]
            else: 
                results['status'] == False
        return results
    
    def creator(self, postData):
        user = self.create(first_name= postData['first_name'], last_name = postData['last_name'], email= postData['email'], password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
        return user

    def validate(self, postData):
        results = {'status': True, 'errors': []}

        if len(postData['first_name']) < 3:
            results['errors'].append('Your first name is too short')
            results['status'] = False

        if len(postData['last_name']) < 3:
            results['errors'].append('Your last name is too short')
            results['status'] = False

        if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
            results['errors'].append('email address is not valid')
            results['status'] = False   

        if postData['password'] != postData['c_password']:
            results['errors'].append('passwords do not match')
            results['status'] = False   
        
        if len(postData['password']) < 5:
            results['errors'].append('Password is too short... should be 5 char or longer')
            results['status'] = False
        
        if len(self.filter(email = postData['email'])) > 0:
            results['errors'].append('User already exists')
            results['status'] = False 

        if not any(char.isalpha() for char in postData['first_name']):
            results['errors'].append('First name must contain at least one character')
            results['status'] = False

        if not any(char.isalpha() for char in postData['last_name']):
            results['errors'].append('Last name must contain at least one character')
            results['status'] = False
        
        if not any(char.isalpha() for char in postData['password']):
            results['errors'].append('Password must contain at least one letter, one number and be at least 7 characters long')
            results['status'] = False

        if not any(char.isdigit() for char in postData['password']):
            results['errors'].append('Password must contain at least one letter, one number and be at least 7 characters long')
            results['status'] = False

        if not any(char.isdigit() for char in postData['password']):
            results['errors'].append('Password must contain at least one letter, one number and be at least 7 characters long')
            results['status'] = False

        if postData['first_name'] == 'Ray' or postData['first_name'] == 'ray':
            results['errors'].append('Yay for Ray!!!')
            results['status'] = False

        # formdate = parser.parse(postData['birthday'])
        # if not len(postData['birthday']):
        #     results['errors'].append("Add a date of birth")
        # elif not formdate <datetime.now():
        #     print "birthday", datetime.now()
        #     results['errors'].append("you can't add a date in the future")
                
        return results


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    # birthday = models.DateField(auto_now=False, auto_now_add=False)
    objects = UserManager()
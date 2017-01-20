from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import User

# Create your models here.
class QuoteManager(models.Manager):
    def create(self, postData):
        alerts = []

        if len(postData['author']) < 1:
            alerts.append('Author cannot be left blank.')
        elif len(postData['author']) < 3:
            alerts.append('Author must be at least 3 characters in length.')

        if len(postData['message']) < 1:
            alerts.append('Message cannot be left blank.')
        elif len(postData['message']) < 10:
            alerts.append('Message must be at least 10 characters in length.')

        if alerts:
            return (False, alerts)
        else:
            user = User.objects.get(id=int(postData['user']))
            # print ('USER:', user.id, user.name)
            quote = Quote.objects.create(user=user, author=postData['author'], message=postData['message'])
            print ('QUOTE:', quote.user.name, quote.author, quote.message)
            return (True, 'success')

    def bridge_connections(self, postData):
        if not postData:
            return (False)
        else:
            user = User.objects.get(id=int(postData['user']))
            quote = Quote.objects.get(id=int(postData['quote']))

            Favorite.objects.create(this_user=user, quote=quote)
            return (True)


    def delete(self, postData):
        if not postData:
            return (False)
        else:
            favorite = Favorite.objects.get(id=int(postData['favorite']))
            favorite.delete()
            return True

    def destroy(self, postData):
        if not postData:
            return (False)
        else:
            delQuote = Quote.objects.get(id=int(postData['quote']))
            delQuote.delete()
            return (True)


class Quote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    author = models.CharField(max_length=255)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quoteManager = QuoteManager()
    objects = models.Manager()

class Favorite(models.Model):
    this_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

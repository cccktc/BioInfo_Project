from django.db import models


    content = models.TextField()

    def __unicode__(self):
        return self.content
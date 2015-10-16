from django.db import models

class Coursetracer(models.Model):

      TermCode = models.IntegerField()
      TermDistr = models.CharField(max_length=100)
      crn = models.IntegerField()
      subj = models.CharField(max_length=3)
      courseNum = models.IntegerField()
      sect = models.IntegerField()
      scheDesc = models.CharField(max_length=50)
      title = models.CharField(max_length=100)
      maxEnroll = models.IntegerField()
      actEnroll = models.IntegerField()

      def getPrompt(self):
          return self .prompt

      def _unicode_ (self):
          return self .prompt

#  class Meta:
#      abstract = True

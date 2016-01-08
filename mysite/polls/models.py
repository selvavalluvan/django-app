from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    combined = models.TextField(null=True, blank=True)
    areas_of_interest = models.ManyToManyField('Interest')

    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text

    def combined_fields(self):
        return '{} :: {}'.format(self.choice_text, self.question)

    def save(self, *args, **kwargs):
        self.combined = self.combined_fields()
        super(Choice, self).save(*args, **kwargs)


class Interest(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __unicode__(self):
        return "Interest: {name}".format(name=self.name)

    class Meta:
        ordering = ['name']


class MemberInterest(models.Model):
    profile = models.CharField(max_length=255, null=True, blank=True)
    interest = models.ForeignKey('polls.Interest')

    def __unicode__(self):
        return "Member: {member}, Interest: {interest}".format(member=self.profile, interest=self.interest.name)
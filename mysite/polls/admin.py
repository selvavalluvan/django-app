from django.contrib import admin
from polls.models import Question, Choice, Interest, MemberInterest

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
        ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    # search_fields = ['question_text', 'choice__choice_text']

class ChoiceAdmin(admin.ModelAdmin):

    list_display = ('choice_text', 'question', 'votes', 'combined')
    search_fields = ['combined']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Interest)
admin.site.register(MemberInterest)
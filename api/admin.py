from django.contrib import admin

from .models import Election, Voter, Candidate


admin.site.register(Election)
admin.site.register(Voter)
admin.site.register(Candidate)


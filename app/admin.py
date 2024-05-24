from django.contrib import admin

from .models import PayoutStatement, AssignmentResult, Result

admin.site.register(AssignmentResult)
admin.site.register(Result)
admin.site.register(PayoutStatement)
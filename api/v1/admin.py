from django.contrib import admin
from api.v1.models import Program, BlackList


class ProgramAdmin(admin.ModelAdmin):
    fields = ('min_credit', 'max_credit',
              'min_age_borrower', 'max_age_borrower')
    list_display = ('id', 'min_credit', 'max_credit',
                    'min_age_borrower', 'max_age_borrower')


class BlackListAdmin(admin.ModelAdmin):
    pass


admin.site.register(Program, ProgramAdmin)
admin.site.register(BlackList, BlackListAdmin)

import requests
from rest_framework.serializers import ValidationError
from api.v1.models import Program, BlackList
from api.v1.helpers import get_current_age


class SumOrderValidator:
    requires_context = True

    def __call__(self, base, serializer):
        data = serializer.parent.initial_data
        program = Program.objects.get(pk=data['program_id'])
        if program.min_credit > base or program.max_credit < base:
            raise ValidationError('Заявка не подходит по сумме')


class AgeOrderValidator:
    requires_context = True

    def __call__(self, base, serializer):
        age = get_current_age(base)
        data = serializer.parent.initial_data
        program = Program.objects.get(pk=data['program_id'])
        if program.min_age_borrower > age or program.max_age_borrower < age:
            raise ValidationError('Заемщик не подходит по возрасту')


class IndividualEntrepreneurValidator:
    url_base = 'https://stat.gov.kz/api/juridical/gov/?bin={iin}&lang=ru'
    requires_context = True

    def __call__(self, base, serializer):
        url = self.url_base.format(iin=base)
        response = requests.get(url)
        if response.status_code != 200:
            raise ValidationError('Не возможно проверить на ИП. Сервис не работает')
        data = response.json()
        if data.get('success', False):
            raise ValidationError('иин является ИП')


class BlackListValidator:
    requires_context = True

    def __call__(self, base, serializer):
        try:
            BlackList.objects.get(iin=base)
            raise ValidationError('Заемщик в черном списке')
        except BlackList.DoesNotExist:
            pass

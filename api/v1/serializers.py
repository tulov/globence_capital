from datetime import datetime
from rest_framework import serializers
from api.v1.models import Program, Order, Borrower
from api.v1.validators import (
    AgeOrderValidator, SumOrderValidator,
    BlackListValidator, IndividualEntrepreneurValidator
)
from api.v1.helpers import get_birthday


class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'max_credit', 'min_credit',
                  'min_age_borrower', 'max_age_borrower',
                  'url']


class OrderPostSerializer(serializers.HyperlinkedModelSerializer):
    program_id = serializers.PrimaryKeyRelatedField(
        queryset=Program.objects.all(),
    )
    iin = serializers.CharField(required=True,
                                source='borrower.iin',
                                validators=(AgeOrderValidator(),
                                            BlackListValidator(),
                                            IndividualEntrepreneurValidator()))
    sum = serializers.IntegerField(required=True,
                                   validators=(SumOrderValidator(),))

    class Meta:
        model = Order
        fields = ['program_id', 'iin', 'sum']

    def create(self, validated_data):
        iin = validated_data['borrower']['iin']
        try:
            borrower = Borrower.objects.get(iin=iin)
        except Borrower.DoesNotExist:
            borrower = Borrower.objects.create(iin=iin,
                                               birthday=get_birthday(iin))
        return Order.objects.create(
            program_id=validated_data['program_id'].id,
            sum=validated_data['sum'],
            borrower=borrower
        )



from django.db import models


class Program(models.Model):
    min_credit = models.IntegerField(null=False, blank=False)
    max_credit = models.IntegerField(null=False, blank=False)
    min_age_borrower = models.IntegerField(null=False, blank=False)
    max_age_borrower = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'Program #{self.id}'


class Borrower(models.Model):
    iin = models.CharField(max_length=12, null=False, blank=False)
    birthday = models.DateField(null=False)

    def __str__(self):
        return self.iin


class Order(models.Model):
    program = models.ForeignKey(Program,
                                related_name='orders',
                                on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower,
                                 related_name='orders',
                                 on_delete=models.CASCADE)
    sum = models.IntegerField(null=False, blank=True)
    status = models.CharField(choices=[('approved', 'одобрено'),
                                       ('rejected', "отказ")],
                              null=True, max_length=12)
    rejection_reason = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return f'Order #{self.id}'


class BlackList(models.Model):
    iin = models.CharField(max_length=12, db_index=True)

    def __str__(self):
        return self.iin

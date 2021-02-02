from django.core.exceptions import ValidationError


def check_phone_number(value):
    phone_number = value.strip().reaplace('+', '')
    if not phone_number.isdecimal():
        raise ValidationError('فرمت شماره وارد شده اشتباه است!')
    elif len(phone_number) != 12:
        raise ValidationError('شماره وارد شده صحيح نمي‌باشد !')


def check_tag(value):
    tags = value.strip().split()
    for i in tags:
        tag = i.replace('#', '')
        tag = tag.replace('_', '')
        if not i.startswith('#'):
            raise ValidationError('فرمت وارد شده براي برچسب ها صحيح نمي‌باشد !')
        elif not tag.isalpha():
            raise ValidationError('فرمت وارد شده براي برچسب ها صحيح نمي‌باشد !')

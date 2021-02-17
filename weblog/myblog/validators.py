from django.core.exceptions import ValidationError


def check_phone_number(value):
    phone_number = value.strip().replace('+', '')
    if not phone_number.isdecimal():
        raise ValidationError('فرمت شماره وارد شده اشتباه است!')
    elif len(phone_number) < 11 or len(phone_number) > 12:
        raise ValidationError('شماره وارد شده صحيح نمي‌باشد !')


def check_tag(value):
    tag = value.strip().replace('#', '').replace('_', '')
    print(tag)
    if not value.startswith('#'):
        raise ValidationError('فرمت وارد شده براي برچسب ها صحيح نمي‌باشد !')
    elif not tag.isalpha():
        raise ValidationError('فرمت وارد شده براي برچسب ها صحيح نمي‌باشد !')
    elif len(value) > 30:
        raise ValidationError('فرمت وارد شده براي برچسب ها صحيح نمي‌باشد !')
    else:
        return True


def check_tag_form(value):
    tag = value.strip().replace('#', '').replace('_', '')
    print(tag)
    if not value.startswith('#'):
        return False
    elif not tag.isalpha():
        return False
    elif len(value) > 30:
        return False
    else:
        return True

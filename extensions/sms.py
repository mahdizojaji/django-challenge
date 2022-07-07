import requests
from random import randint

from django.conf import settings


def generate_random_code():
    length = settings.SMS['OTP_LENGTH']
    code = ''.join([f'{randint(0, 9)}' for _ in range(length)])
    return code


def raw_verification_request(apikey, receptor, type_, template, check_id, **params):
    url = "https://api.ghasedak.me/v2/verification/send/simple"
    headers = {
        'apikey': apikey,
        'cache-control': "no-cache",
        'content-type': "application/x-www-form-urlencoded",
    }
    payload = {
        'type': type_,
        'receptor': receptor,
        'template': template,
        'checkid': check_id,
        **params
    }
    response = requests.post(url=url, data=payload, headers=headers)
    return response


def send_otp_sms(phone_number, *params, check_id=None):
    kwargs = {
        'type_': 1,
        'check_id': check_id,
        'receptor': phone_number,
        'apikey': settings.SMS['API_KEY'],
        'template': settings.SMS['TEMPLATE_NAME'],
    }
    if check_id:
        kwargs.update({'checkid': check_id})
    if len(params) not in range(1, 11):
        raise ValueError('params count not in range 1...10')
    for index, param in enumerate(params, start=1):
        kwargs.update({f'param{index}': param})
    return raw_verification_request(**kwargs)

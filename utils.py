from kavenegar import *

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('4D48706B66523733496D4B7835416C594C50596F5264562B30414B384371314C773335615A4A2B6B3562513D')
        params = {
            'sender': "2000660110",
            'receptor': phone_number,
            'message': f'{code}کد تایید شما',
        }
        response = api.sms_send(params)
        print(response)

    except APIException as e:
        print(e)

    except HTTPException as e:
        print(e)
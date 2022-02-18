# ---------------------------------------------------------------
# This program shows how to generate a 64-bit secret key for a certain
# user, as well as to generate a QRcode for this user.
# Written by Yingli Zhao, February 2022
# ---------------------------------------------------------------
import pyotp
from qrcode import QRCode, constants
import os
import traceback


def get_qrcode(secret_key, username):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dirpath = os.path.join(BASE_DIR, 'htmlParser', 'static')
#   os.mkdir("/Users/xuhengwang/PycharmProjects/mfa/") # permission of the new folder will not be inherited from parent folder in MacOS. This will be done later.
#   Therefore, the dirpath have been created manuelly in advance.

    data = pyotp.totp.TOTP(secret_key).provisioning_uri(username, issuer_name="IAM MFA Code")
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=6,
        border=4)
    try:
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        filepath = dirpath + os.sep + secret_key + '.png'
        filepath_part = '../static' + os.sep + secret_key + '.png'
        img.save(filepath)  # save qrcode
        return True, filepath_part
    except Exception as e:
        traceback.print_exc()
        return False, None


def generate_gtoken():
    gtoken = pyotp.random_base32(64)  # get secret key, can be saved in usertable in database, 64 bits
    return gtoken


def transfer_gtoken(gtoken):
    return gtoken


if __name__ == "__main__":
    gtoken = generate_gtoken()    #get secret key 获取随机密钥，存于用户表中,随机64位
    result = get_qrcode(gtoken, 'chunyuwang1@gmail.com')    # generate qr code by using secret key


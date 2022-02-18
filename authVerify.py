# ---------------------------------------------------------------
# This program shows if a verifycode from client is matching
# for a secret key on Webserver.
# Written by Yingli Zhao, February 2022
# ---------------------------------------------------------------
import pyotp


def Google_Verify_Result(secret_key, verifycode):
    t = pyotp.TOTP(secret_key)
    result = t.verify(verifycode)  # 对输入验证码进行校验，正确返回True
    msg = result if result is True else False
    return msg


#if __name__ == "__main__":
#    verifycode = input('Enter your verifycode: ')
#    gtoken = "IQAYWR7HIHGOGABVFYYTXRMCCZIYGHB63VICSINDLBSG7WUHOHXFYBU5O3YQCAOO"
#    msg = Google_Verify_Result(gtoken, verifycode)
#    print(msg)

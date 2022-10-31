# -*- coding: utf-8 -*-

# 打卡脚修改自ZJU-nCov-Hitcarder的开源代码，感谢这位同学开源的代码

import requests
import json
import re
import datetime
import random
import time
import sys
import ddddocr


class ClockIn(object):
    """Hit card class
    Attributes:
        username: (str) 川大微服务平台用户名（一般为学号）
        password: (str) 川大微服务平台密码
        LOGIN_URL: (str) 登录url
        BASE_URL: (str) 打卡首页url
        SAVE_URL: (str) 提交打卡url
        HEADERS: (dir) 请求头
        sess: (requests.Session) 统一的session
    """
    LOGIN_URL = "https://ua.scu.edu.cn/login?service=https%3A%2F%2Fwfw.scu.edu.cn%2Fa_scu%2Fapi%2Fsso%2Fcas-index%3Fredirect%3Dhttps%253A%252F%252Fwfw.scu.edu.cn%252Fncov%252Fwap%252Fdefault%252Findex"
    BASE_URL = "https://wfw.scu.edu.cn/ncov/wap/default/index"
    SAVE_URL = "https://wfw.scu.edu.cn/ncov/wap/default/save"
    CAPTCHA_URL = 'https://ua.scu.edu.cn/captcha?captchaId='
    NUCLEIC_ACID_URL = 'https://wfw.scu.edu.cn/form/wap/default/save'
    HEADERS = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36" }
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.sess = requests.Session()
        self.ocr = ddddocr.DdddOcr()

    def login(self):
        """Login to SCU platform"""
        res = self.sess.get(self.LOGIN_URL, headers=self.HEADERS)
        execution = re.search(
            'name="execution" value="(.*?)"', res.text).group(1)

        captcha_id = re.search(
                'id: \'(.*?)\'', res.text).group(1)

        self.CAPTCHA_URL += captcha_id
        captcha = self.get_captcha()

        data = {
            'username': self.username,
            'password': self.password,
            'captcha': captcha,
            'submit': '%E7%99%BB%E5%BD%95',
            'type': 'username_password',
            'execution': execution,
            '_eventId': 'submit'
        }
        res = self.sess.post(url=self.LOGIN_URL, data=data, headers=self.HEADERS)

        # check if login successfully
        
        if res.status_code!=requests.codes.ok:
            raise LoginError('登录失败，请核实账号密码或稍后重试')

        return self.sess

    def post_ncov_testing(self):
        """Post the testing record"""
        ncov_test = {"id":"124", "body[id]":"", "body[9yue20rizuorishifouyizuohesuan]":"是"}
        res = self.sess.post(self.NUCLEIC_ACID_URL, data=ncov_test, headers=self.HEADERS)
        return json.loads(res.text)

    def post_info(self):
        """Post the hitcard info"""
        res = self.sess.post(self.SAVE_URL, data=self.info, headers=self.HEADERS)
        return json.loads(res.text)

    def get_date(self):
        """Get current date"""
        today = datetime.date.today()
        return "%4d%02d%02d" % (today.year, today.month, today.day)

    def get_captcha(self):
        """Get CAPTCHA code"""
        resp = self.sess.get(self.CAPTCHA_URL)
        captcha = self.ocr.classification(resp.content)
        print("验证码：", captcha)
        return captcha

    def get_info(self, html=None):
        """Get hitcard info, which is the old info with updated new time."""
        if not html:
            res = self.sess.get(self.BASE_URL, headers=self.HEADERS)
            html = res.content.decode()

        try:
            old_infos = re.findall(r'oldInfo: ({[^\n]+})', html)
            if len(old_infos) != 0:
                old_info = json.loads(old_infos[0])
            else:
                raise RegexMatchError("未发现缓存信息，请先至少手动成功打卡一次再运行脚本")

        except IndexError:
            raise RegexMatchError('Relative info not found in html with regex')
        except json.decoder.JSONDecodeError:
            raise DecodeError('JSON decode error')

        new_info = old_info.copy()
        new_info["date"] = self.get_date()
        new_info["created"] = round(time.time())

        self.info = new_info
        return json.loads(old_info["geo_api_info"])["formattedAddress"]

# Exceptions
class LoginError(Exception):
    """Login Exception"""
    pass


class RegexMatchError(Exception):
    """Regex Matching Exception"""
    pass


class DecodeError(Exception):
    """JSON Decode Exception"""
    pass


def main(username, password, times):
    """Hit card process
    Arguments:
        username: (str) 川大微服务平台用户名（一般为学号）
        password: (str) 川大微服务平台密码
        times: 打卡次数
    """

    print("🎲考虑下打不打卡")

    abort = True
    rnd = random.randint(1, times)

    if rnd == times: # 在每天的<times>个时间点以<1/times>的概率执行打卡
        abort = False
        print("✅yesyes!")

    now = int(time.time())
    if (now/3600 % 24 + 8) > 18: # 在18:00之后补打一次
        abort = False
        print("✅补打一个")

    if abort:
        print("✅下次一定")
        #sys.exit(0)
    

    print("\n[Time] %s" %
          datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("🚌 打卡任务启动")

    dk = ClockIn(username, password)

    print("登录到川大微服务平台...")
    for i in range(10):
        try:
            if i != 0:
                print("🔮刷新验证码，重新登录...")
            dk.login()
            print("✅已登录到川大微服务平台")
            break;
        except Exception as err:
            if i == 9:
                raise Exception("❌",str(err))

    print("正在填报核酸检测记录...")
    try:
        res = dk.post_ncov_testing()
        print("✅", res['m'])
        if str(res['e']) == '1':
            raise Exception("❌核酸检测填报失败: "+res['m'])
    except Exception:
        raise Exception("❌核酸检测填报失败: 未知错误")

    print('正在获取上次打卡信息...')
    try:
        location = dk.get_info()
        print("✅", location)
    except Exception as err:
        raise Exception("❌获取信息失败，请手动打卡，更多信息: " + str(err))

    print("正在为您打卡...")
    try:
        res = dk.post_info()
        if str(res['e']) == '1':
            if res['m'].find("已经") != -1: # 已经填报过了 不报错
                pass
            else:
                raise Exception("❌数据提交失败: "+res['m'])
        print("✅",res['m'])
    except Exception:
        print('❌数据提交失败')
        raise Exception


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    times = sys.argv[3]
    cnt = 0
    try:
        main(username, password, int(times))
    except Exception as err:
        print(err)

import time
import datetime
import hashlib
import random

"""常用量获得"""

__all__ = ['getUnix_timeTuple', 'getMD5']

def getUnix_timeTuple(date=datetime.datetime.now()):
    """获得unix 时间戳"""
    return time.mktime(date.timetuple())

def getDateFromTimeTuple(unix_time=0, formatter='%Y-%m-%d %H:%M:%S') -> time:
    """时间戳转换成时间"""
    t = int(unix_time)
    time_locol = time.localtime(t)
    return time.strftime(formatter, time_locol)

def getMD5(code):
    """获得md5加密的字符串"""
    if code:
        md5string = hashlib.md5(code.encode('utf-8'))
        return md5string.hexdigest()
    return None

def get_random_num(digit=6):
    """获得一个随机数"""
    if digit is None:
        digit = 1
    digit = min(digit, 10)# 最大支持10位
    result = ""
    while len(result) < digit:
        append = str(random.randint(1, 9))
        result = result + append
    return result

def get_list_from_column(content):
    if content is None:
        return None
    content = str(content)
    while content.startswith(';'):
        content = content[1: ]
    while content.endswith(';'):
        content = content[:-1]
    return content.split(';')
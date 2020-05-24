# -*- coding: utf-8 -*-
import random
#定义返回32位的随机数，包含大小写字母，数字
def v_code():
    ret = ""
    for i in range(32):
        num = random.randint(0, 9)
        # num = chr(random.randint(48,57))#ASCII表示数字
        letter = chr(random.randint(97, 122))#取小写字母
        Letter = chr(random.randint(65, 90))#取大写字母
        s = str(random.choice([num,letter]))
        ret += s
    return ret
uuid=v_code()
print(uuid)
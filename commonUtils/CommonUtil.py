#! python3
# -*- coding:utf-8 -*-
from pypinyin import pinyin,lazy_pinyin
import pypinyin


# 提取中文拼音首字母
def get_first_letter(param):
    if param is not None and len(param) > 0:
        piny_list = pinyin(param, style=pypinyin.INITIALS)
        first_letter = piny_list[0][0]
        if len(first_letter) > 0:
            first_letter = first_letter[0: 1]
        return first_letter
    else:
        return None
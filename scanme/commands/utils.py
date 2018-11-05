import os
from functools import reduce
import operator


def get_from_dict(data, map_list):
    return reduce(operator.getitem, map_list, data)

def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


def dir_metatree(_ROOT_='.'):

    _LEAF_ = {'*': ''}
    data = {}

    for dirName, subdirList, fileList in os.walk(_ROOT_):

        dirPath = dirName.split('/')[1:]

        try:
            get_from_dict(data, dirPath)
        except:
            nested_set(data, dirPath, _LEAF_)

        for fname in fileList:

            if dirPath:
                nested_set(data, dirPath, {fname: _LEAF_})

            else:
                data[fname] = _LEAF_

    return data

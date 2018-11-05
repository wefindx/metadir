import os
from functools import reduce
import operator
import copy


def get_from_dict(data_dict, map_list):
    return reduce(operator.getitem, map_list, data_dict)

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
            nested_set(data, dirPath, copy.copy(_LEAF_))

        for fname in fileList:

            if dirPath:
                nested_set(data, dirPath, {fname: copy.copy(_LEAF_)})

            else:
                data[fname] = copy.copy(_LEAF_)

    return data



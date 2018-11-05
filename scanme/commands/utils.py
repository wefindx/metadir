import os
import copy


def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {'*': ''})
    dic[keys[-1]] = value


def dir_metatree(_ROOT_='.'):

    _LEAF_ = {'*': ''}

    data = copy.copy(_LEAF_)

    for dirName, subdirList, fileList in os.walk(_ROOT_):
        dirPath = dirName.split('/')[1:]

        for fname in fileList:
            if dirPath:
                nested_set(data, dirPath+[fname], copy.copy(_LEAF_))
            else:
                data[fname] = copy.copy(_LEAF_)

    return data



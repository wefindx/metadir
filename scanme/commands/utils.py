import os

def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


def dir_metatree(_ROOT_='.'):

    _LEAF_ = {'*': ''}
    data = {}

    for dirName, subdirList, fileList in os.walk(_ROOT_):

        dirPath = dirName.split('/')[1:]

        tree = {}
        for k in reversed(dirPath):
            tree = dict(_LEAF_, **{k: tree})

        data.update(tree)

        for fname in fileList:

            if dirPath:
                nested_set(data, dirPath, {fname: _LEAF_})

            else:
                data[fname] = _LEAF_

    return data

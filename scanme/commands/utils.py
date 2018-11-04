import os

def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


def dir_metatree(
        _ROOT_='.',
        ignore_dot_files=True,
        ignore_extensions=['.pyc', '.tar.gz'],
        ignore_dirs=['__pycache__', '.egg-info', 'dist']
    ):

    _LEAF_ = {'*': ''}
    data = {}

    for dirName, subdirList, fileList in os.walk(_ROOT_):

        # SKIP
        if dirName.startswith('./.') and ignore_dot_files:
            continue

        dirPath = dirName.split('/')[1:]

        # SKIP
        if dirPath:
            if any([dirPath[-1].endswith(ignore) for ignore in ignore_dirs]):
                continue

        tree = {}
        for k in reversed(dirPath):
            tree = dict(_LEAF_, **{k: tree})

        data.update(tree)

        for fname in fileList:

            # SKIP
            if any([fname.endswith(ignore) for ignore in ignore_extensions]):
                continue

            if dirPath:
                nested_set(data, dirPath, {fname: _LEAF_})

            else:
                data[fname] = _LEAF_

    return data

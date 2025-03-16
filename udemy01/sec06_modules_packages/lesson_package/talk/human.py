from lesson_package.tools import utils
# from ..tools import utils
# 非推奨：../を使うと、ディレクトリ構造が変わった場合にエラーが発生する可能性がある。


def sing():
    return 'sing'


def cry():
    return utils.say_twice('cry')

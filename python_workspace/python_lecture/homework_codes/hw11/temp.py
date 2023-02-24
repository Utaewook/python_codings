import sys


def this_is_what():
    print("함수 이름은: {}".format(sys._getframe().f_code.co_name))

this_is_what()


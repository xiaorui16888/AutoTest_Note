from hytest import INFO
force_tags = ['功能测试']

def suite_setup():
    INFO('总初始化')
    pass

def suite_teardown():
    INFO('总清除')
    pass


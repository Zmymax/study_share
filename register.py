# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

# touch(Template(r"tpl1635500814206.png", record_pos=(-0.398, -0.1), resolution=(1920, 1080)),times=2,duration=0.01,click_right=False)


touch(Template(r"tpl1635500069922.png", record_pos=(-0.115, -0.225), resolution=(1920, 1080)))

sleep(2)

touch(Template(r"tpl1635500078609.png", record_pos=(-0.395, -0.077), resolution=(1920, 1080)))

text("13@qq.com")
touch(Template(r"tpl1635500096161.png", record_pos=(-0.39, -0.048), resolution=(1920, 1080)))

text("8953E5-C77E41-763E67-A545DC-FD4606FF")

touch(Template(r"tpl1635500127401.png", record_pos=(-0.225, -0.014), resolution=(1920, 1080)))

sleep(5)



touch(Template(r"tpl1635500556538.png", record_pos=(-0.011, -0.249), resolution=(1920, 1080)))

touch(Template(r"tpl1635500561650.png", record_pos=(0.019, -0.248), resolution=(1920, 1080)))

touch(Template(r"tpl1635500758503.png", record_pos=(-0.044, -0.255), resolution=(1920, 1080)))


assert_exists(Template(r"tpl1635500204534.png", record_pos=(-0.31, -0.079), resolution=(1920, 1080)), "注册失败")


assert_not_exists(Template(r"tpl1635500204534.png", record_pos=(-0.31, -0.079), resolution=(1920, 1080)),  "注册成功")

touch(Template(r"tpl1635500416931.png", record_pos=(-0.148, 0.058), resolution=(1920, 1080)))



#!/usr/bin/python3
# coding: utf-8


from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from ssh import get_space
from ssh import getIfconfig
from ssh import getDmi
from ssh import parseIfconfig
from ssh import getHostname
from ssh import getCpu
import time

t1 = time.time()
# qq邮箱smtp服务器
host_server = 'smtp.163.com'
# sender_qq为发件人的qq号码
sender_qq = '13805762413'
# pwd为qq邮箱的授权码
pwd = 'flzx3qcasd'
# 发件人的邮箱
sender_qq_mail = '13805762413@163.com'
# 收件人邮箱
receiver = '18855105981@163.com'
#receiver = '1224049792@qq.com'
#receiver = '1205997930@qq.com'
#receiver = '136305163@qq.com'
# receiver = '917366034@qq.com'

# 获取根目录的使用率
use_space=get_space()
    # print(use_space)
    # dic = {}
data_ip = getIfconfig()
parsed_data_ip = parseIfconfig(data_ip)
Memorys = getCpu()
hostnames = getHostname()
a='''welcome, 你的根目录使用率为%s，空间正常 \n
IP  : %s,   BCAST  : %s,  MASK   :%s \n
Memory : %s \n
hostname: %s \n
'''%(use_space, parsed_data_ip[0], parsed_data_ip[1],parsed_data_ip[2],Memorys,hostnames)


# 邮件的正文内容
mail_content = "%s"%a
# 邮件标题
mail_title = '207.246.73.178服务器运行情况'

# ssl登录
smtp = SMTP_SSL(host_server)
# set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = receiver
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()


t2 = time.time()
print(t2-t1)

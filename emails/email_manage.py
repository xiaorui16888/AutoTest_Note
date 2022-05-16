# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：email_manage.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/15 13:59
"""
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailManage:

    def send_email(self, report_name):
        # 定义SMTP服务器
        smtp_server = 'smtp.163.com'
        # 发送邮件的用户名和客户端密码
        username = 'wr87920151@163.com'
        password = 'DFREVXVTPUTIYZZR'
        # 接受邮件的邮箱
        receiver = '87920151@qq.com'
        # 创建邮件对象
        message = MIMEMultipart('related')
        subject = '上海公安一网通项目自动化测试报告'  # 邮件的主题
        with open(report_name, 'rb') as f:
            mail_body = f.read()
        body = MIMEText(_text=mail_body, _subtype='html', _charset='utf-8')  # 附件
        message['form'] = username
        message["to"] = ",".join(receiver)
        message['subject'] = subject
        message.attach(body)
        # 添加附件
        att = MIMEText(open(report_name, "rb").read(), "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename= "report.html"'
        message.attach(att)
        # 登录smtp服务器并发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server)
        smtp.login(username, password)
        smtp.sendmail(username, receiver, message.as_string())
        smtp.quit()


if __name__ == '__main__':
    em = EmailManage()
    em.send_email(report_name=os.getcwd() + '/report.html')

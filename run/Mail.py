#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from Global.Global import logger
import sys
sys.path.append('../')

def get_mail_list(startNO=100000, count=1, mail_prefix='@qq.com'):
    '''生成邮箱账号列表'''
    return [str(x) + mail_prefix for x in xrange(startNO + count) if x >= startNO]

class Mail:
    def __init__(self,from_,to_,pwd,subject,msg,host='smtp.qq.com',port=465):
        self.start_time = time.time()
        self.from_ = from_
        self.to_ = to_
        self.pwd = pwd
        self.msg = msg
        self.host =host
        self.port = port
        self.subject = subject
        self.__getsmtpObj__()
        self.login()
        
    def __getsmtpObj__(self):
        '''get smtp obj'''
        if self.port == 25:
            self.smtpObj = smtplib.SMTP()
    
        else:
            self.smtpObj = smtplib.SMTP_SSL(self.host, self.port)

    def send_mail(self):
        '''
        :param mail_host:
        :param from_:
        :param to_:
        :param subject:
        :param msg:
        :return:
        '''
        try:
            message = MIMEMultipart('related')
            message['From'] = self.from_
            message['To'] = Header('TA', 'utf-8')
            subject = self.subject
            message['Subject'] = Header(subject, 'utf-8')
            msgAlternative = MIMEMultipart('alternative')
            message.attach(msgAlternative)
            msgAlternative.attach(MIMEText(self.msg, 'html', 'utf-8'))
            # 指定图片为当前目录
            fp = open('./Data/xinbao.png', 'rb')
            msgImage = MIMEImage(fp.read())
            fp.close()
            # 定义图片 ID，在 HTML 文本中引用
            msgImage.add_header('Content-ID', '<image1>')
            # 添加附件
            message.attach(msgImage)
            
            self.smtpObj.sendmail(self.from_, self.to_, message.as_string())
            logger.debug("成功发送 【 %d 】 封邮件" % len(self.to_))
            cost_time = time.time() - self.start_time
            cost_time = round(cost_time, 3)
            # print cost_time
            logger.debug('总用时：%s 秒' % str(cost_time))
        except smtplib.SMTPException as e:
            logger.error(e)
            raise
        finally:
            self.smtpObj.quit()
    
    def login(self):
        '''
        :param mail_host:
        :param usr:
        :param pwd:
        :return:
        '''
        self.smtpObj.connect(self.host, self.port)  # port 为 SMTP 端口号
        s = self.smtpObj.login(self.from_, self.pwd)
        # print s
        if s[0] == 235:
            logger.debug('邮箱登录成功')
        


if __name__=='__main__':
    # 第三方 SMTP 服务
    # mail_host = "smtp.163.com"  # 设置服务器
    # mail_user="18589091413@163.com"    #用户名
    # mail_pass="zhang6246593"   #口令
    
    # mail_user="2571226011@qq.com"    #用户名
    # mail_pass="qmyjbocqbmoyecbe"   #授权码
    
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "372233740@qq.com"  # 用户名
    mail_pass = "hcpsrobckaetbjbi"  # 授权码
    prefix = '@qq.com' # 指定邮件后缀
    mail_port = 465
    sender = mail_user
    # receivers = ['373743261@qq.com','18589091413@163.com','575735@qq.com','372233740@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    receivers = get_mail_list(373743261,1,prefix)
    subject = "新 宝 集 团"
    mail_msg = """
	 <p>
	 如果您的朋友所在平台投注超过 1秒，邀请他来新宝GG体验五星10W注秒投.<br>
	 如果您的朋友所在平台开奖派彩超过30秒，邀请他来新宝GG体验什么是秒级返奖.<br>
	 如果您的朋友所在平台提款超过60秒，邀请他来新宝GG体验什么是秒级出款.<br>
	 如果您的朋友所在平台充值常不到账，邀请他来新宝GG体验什么是秒级到账.<br>
	 如果您的朋友所在平台访问速度很慢，邀请他来新宝GG体验什么是飞一般的感觉.<br>
	 新宝GG，我们追求的就是速度快！速度快，心情就愉快，玩得就更痛快！<br>
	 <br>
	 云龙团队，信誉 稳定 安全 <br>
	 给力计划！软件  应有尽有！<br>
	<br>
	做新宝认准 云龙 qq：575735 <br>
	</p>
	 <p><a href="http://666.xbgg1.com/index.php?s=/WebPublic/register/code/31849b9a2d34228cf4cb024bf9fa07ff/plf/link/">快速入口</a></p>

	<p>使用手机浏览器扫码加入吧：</p>
	<p><img src="cid:image1"></p>

	"""
    
    mail = Mail(mail_user,receivers,mail_pass,subject,mail_msg,mail_host,mail_port)
    mail.send_mail()
    
    

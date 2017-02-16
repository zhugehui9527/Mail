# -*- coding:utf-8 -*-
from run.Mail import *

# 第三方 SMTP 服务
# mail_host = "smtp.163.com"  # 设置服务器
# mail_user="18589091413@163.com"    #用户名
# mail_pass="zhang6246593"   #口令

# mail_user="2571226011@qq.com"    #用户名
# mail_pass="qmyjbocqbmoyecbe"   #授权码

mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "372233740@qq.com"  # 用户名
mail_pass = "hcpsrobckaetbjbi"  # 授权码
prefix = '@qq.com'  # 指定邮件后缀
mail_port = 465
sender = mail_user
# receivers = ['373743261@qq.com','18589091413@163.com','575735@qq.com','372233740@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = get_mail_list(373743261, 1, prefix)
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

mail = Mail(mail_user, receivers, mail_pass, subject, mail_msg, mail_host, mail_port)
mail.send_mail()



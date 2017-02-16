# -*- coding:utf-8 -*-
#######################################################
#filename:Run_conf.py
#author:Jeff
#date:2016-09
#function:运行加载配置数据
#######################################################
import os
import ConfigParser

prjDir = os.path.split(os.path.realpath(__file__))[0]
conf_path = os.path.join(prjDir, "conf.ini")

#加载配置文件
def load_config(file_path):
	config = ConfigParser.ConfigParser()
	try:
		if os.path.exists(file_path):
			config.read(file_path)
			return config
	except:

		print "%s is not exits",file_path

#读取cfg文件中的seciton区域中的某一个option值并返回该值
def read_config(section_name,option):
	monitor_cfg = load_config(conf_path)
	for section in monitor_cfg.sections():
		if section == section_name:
			value = monitor_cfg.get(section,option)
			return value
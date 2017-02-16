# -*- coding:utf-8 -*-
from log.log import LogSignleton
Log = LogSignleton()
logger = Log.get_logger()

class L:
	logger = None
	@classmethod
	def set_logger(cls,logger):
		cls.logger = logger
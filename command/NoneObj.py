#-*- coding: utf-8 -*-

class NoneObj:

	category = 'none'

	commandName = ' '
	description = '不正入力'

	env = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self):
		print 'executed None'

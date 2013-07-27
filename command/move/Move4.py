#-*- coding: utf-8 -*-
import os
import os.path

class Move4:

	category = 'move'

	commandName = '4'
	description = '画面１ 左半分'

	left = 0
	top = 0
	width = 960
	height = 1080

	env = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self):
		scriptPath = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../../script')
		scriptType = 'move'
		scriptName = 'win.exe'

		script = '"%s/%s/%s"' % (scriptPath, scriptType, scriptName)

		os.system('%s %s %s %s %s' % (script, self.left, self.top, self.width, self.height))

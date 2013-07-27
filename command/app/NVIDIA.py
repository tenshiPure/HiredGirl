#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class NVIDIA(Base):

	category = 'app'

	commandName = 'nva'
	description = 'NVIDIA'

	appName  = 'nvcplui.exe'
	appPath  = r'C:\Program Files\NVIDIA Corporation\Control Panel Client\nvcplui.exe'
	winClass = 'NVIDIA'

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self, isNew = None):
		scriptName = 'active' if isNew is None else 'new'
		script = self.createScriptPath(scriptName)

		self.executeAppScript(script)

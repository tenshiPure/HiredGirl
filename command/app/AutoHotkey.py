#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class AutoHotkey(Base):

	category = 'app'

	commandName = 'ahk'
	description = 'AutoHotkey'

	appName  = 'ahk'
	appPath  = r'C:\Program Files\AutoHotkey\AutoHotKeyU64.exe'
	winClass = ''

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self, isNew = None):
		scriptName = 'active' if isNew is None else 'new'
		script = self.createScriptPath(scriptName)

		self.executeAppScript(script)

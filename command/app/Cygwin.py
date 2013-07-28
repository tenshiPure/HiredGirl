#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Cygwin(Base):

	category = 'process'

	commandName = 'cyg'
	description = 'Cygwin'

	appName  = 'Cygwin.bat'
	appPath  = r'C:\cygwin\Cygwin.bat'
	winClass = 'ahk_class ConsoleWindowClass'

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self, isNew = None):
		scriptName = 'active' if isNew is None else 'new'
		script = self.createScriptPath(scriptName)

		self.executeAppScript(script)

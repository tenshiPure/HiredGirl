#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class DeSmuME(Base):

	category = 'process'

	commandName = 'ds'
	description = 'DeSmuME'

	appName  = 'DeSmuME.exe'
	appPath  = r'D:\Game\emulator\DS\desmume-0.9.8-win32\DeSmuME.exe'
	winClass = 'DeSmuME'

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self, isNew = None):
		scriptName = 'active' if isNew is None else 'new'
		script = self.createScriptPath(scriptName)

		self.executeAppScript(script)

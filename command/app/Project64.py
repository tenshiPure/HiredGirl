#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Project64(Base):

	category = 'process'

	commandName = 'pj'
	description = 'Project64'

	appName  = 'Project64k.exe'
	appPath  = r'C:\Program Files\Project64k\Project64k.exe'
	winClass = 'Project64k Version 0.13 Core 1.4'

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self, isNew = None):
		scriptName = 'active' if isNew is None else 'new'
		script = self.createScriptPath(scriptName)

		self.executeAppScript(script)

#-*- coding: utf-8 -*-
import os
import os.path
import sys

pathNone = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(os.path.abspath(pathNone))
from Base import Base

class Trash(Base):

	category = 'process'

	commandName = 'trash'
	description = 'Trash'

	dirPath  = r'C:\$Recycle.Bin\S-1-5-21-1672928867-819109563-735477428-500'

	executableEnv = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# 実行
	#
	def execute(self, isNew = None):
		scriptName = 'active' if isNew is None else 'new'
		script = self.createScriptPath(scriptName)

		print script
		self.executeDirScript(script)

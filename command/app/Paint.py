#-*- coding: utf-8 -*-
import os
import os.path

class Paint:

	category = 'app'

	commandName = 'paint'
	description = 'Paint'

	exeName = 'mspaint.exe'
	exePath = r'C:\Windows\System32\mspaint.exe'
	winClass = 'MSPaintApp'

	env = ['ryowin', 'nebigwin', 'nebigmac']

	#
	# é¿çs
	#
	def execute(self, isNew = None):
		scriptPath = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../../script')
		scriptType = 'active'
		scriptName = 'win.exe'

		script = '"%s/%s/%s"' % (scriptPath, scriptType, scriptName)

		os.system('%s %s %s %s' % (script, self.exeName, self.exePath, self.winClass))

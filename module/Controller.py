#-*- coding: utf-8 -*-
import sys
from CommandAnalyser import CommandAnalyser

class Controller:

	#
	# コンストラクタ
	#
	def __init__(self, input):
		analyser = CommandAnalyser()
		input1, input2, input3 = analyser.splitInput(input)

		command1, command2, command3 = analyser.createCommand(input1, input2, input3)

		if not analyser.isExecutableInput(command1, command2, command3):
			print 'invalid inputs'
			return

		if command3.commandName == 'new':
			command1.execute('new')
		elif command1.commandName == 'ss':
			command1.execute(input2)
		else:
			command1.execute()
		command2.execute()

inputed = sys.argv[1]
controller = Controller(inputed)

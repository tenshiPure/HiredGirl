#-*- coding: utf-8 -*-
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
		else:
			command1.execute()
		command2.execute()

input = 'paint 4'
controller = Controller(input)

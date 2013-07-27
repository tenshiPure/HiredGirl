#j::
	InputBox, inputed, Hired Girl, , , 150, 100, 1750, 20

	StringReplace, replaced, inputed, %A_Space%, _, All

	Run, "D:\MyDocument\Program\HiredGirl\module\Controller.py" %replaced%
return

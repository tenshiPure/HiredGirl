name = %1%
path = %2%
win  = %3%

Process, Exist, %name%

if ErrorLevel <> 0
	WinActivate, ahk_pid %ErrorLevel%

else {
	Run, %name%
	WinWait, ahk_class %win%, , 1, ,
}

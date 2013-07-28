WinGetTitle, winTitle, A

IfInString, winTitle, JoyToKey
{
	WinActivate, ahk_class TMainForm
	Send, {Alt}fx
}

else
{
	WinKill, A
}

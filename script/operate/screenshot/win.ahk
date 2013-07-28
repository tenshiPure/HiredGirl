paintPath = %1%
paintWin  = %2%
fileName  = %3%

FormatTime, timestamp, , 'ScreenShot'_yyyyMMdd_HHmmss_

filename := timestamp . fileName 

Send, {PrintScreen}
Run, %paintPath%
WinWait, ahk_class %paintWin%, , 1, ,
Send, ^v
Send, ^s
WinWait, ahk_class #32770
Send, D:\MyPicture\ScreenShot\%fileName%.png
Send, {Enter}
WinWait, ahk_class %paintWin%, , 1, ,
WinKill, A

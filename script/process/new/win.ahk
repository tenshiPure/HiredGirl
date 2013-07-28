name = %1%
path = %2%
win  = %3%

StringReplace, name, name, _space_, %A_Space%, All
StringReplace, path, path, _space_, %A_Space%, All
StringReplace,  win,  win, _space_, %A_Space%, All

Run, %path%
WinWait, ahk_class %win%, , 1, ,

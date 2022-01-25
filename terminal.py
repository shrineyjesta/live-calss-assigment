Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:37:30) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import subprocess
>>> subprocess.call("calc.exe")
0
>>> subprocess.call("IDLE.exe")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    subprocess.call("IDLE.exe")
  File "C:\Users\SHRINEY JESTA J\AppData\Local\Programs\Python\Python38-32\lib\subprocess.py", line 340, in call
    with Popen(*popenargs, **kwargs) as p:
  File "C:\Users\SHRINEY JESTA J\AppData\Local\Programs\Python\Python38-32\lib\subprocess.py", line 854, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "C:\Users\SHRINEY JESTA J\AppData\Local\Programs\Python\Python38-32\lib\subprocess.py", line 1307, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
FileNotFoundError: [WinError 2] The system cannot find the file specified
>>> subprocess.call("C://Program Files//VideoLAN//VLC//vlc.exe")
0
>>> 
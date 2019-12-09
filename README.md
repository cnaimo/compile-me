# compile-me
[![HitCount](http://hits.dwyl.io/cnaimo/compile-me.svg)](http://hits.dwyl.io/cnaimo/compile-me) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub pull-requests](https://img.shields.io/github/issues-pr/Naereen/StrapDown.js.svg)](https://github.com/cnaimo/compile-me/pull/)  [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/cnaimo/compile-me/issues/)

This script helps avoid having to set up a compiler in your preferred IDE or manually entering compile parameters into your Linux terminal every time you want to compile and run your project.

# v1.2.0 is out!
Check it out in the releases tab. Additional functionality is included to enable/disable sudo command for running your compiled C/C++ project. I believe GCC/G++ utilizes identical commands on mac, if anyone can confirm mac compatibility that would be a major help.

# Usage
Clone this repository and place compile.py in the directory of the C/C++ project that you would like to compile and run. In compile.py edit the following as needed:

```python
compiler = 'g++' # g++ for C++, gcc for C
file_to_compile = 'example.cpp' 
libraries_to_link = ['curl', 'jsoncpp'] # add any required libraries here, if none then leave as []
libraries_that_need_compiling = ['my_library.cpp'] # any cpp/c libraries in your project that you need compiled and linked
```

Run compile.py in Linux terminal in the directory of your project:
```
cd /your/project/directory
python3 compile.py
```
Press the "enter" key when you're ready to compile and run your project. You can keep this script running in the background while you work on your projects and use it to re-compile and run as needed. You can stop the script via KeyboardInterrupt by pressing 'ctrl' + 'c' or simply exit out the terminal. The 'ctrl' + 'c' combination can also be used to quit the C/C++ program while it is running.

When promped with ```Compile and run me? (ENTER)```, entering ```sudo run``` or ```disable sudo``` will enable and disable sudo for executing your compiled project, respectively. Any changes made in compile.py will not take effect until compile.py is restarted in the Linux Terminal.

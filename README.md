[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
# compile-me
This script helps avoid having to set up a compiler in your preferred IDE or manually entering compile parameters into your Linux terminal every time you want to compile and run your project.

# Usage
Clone this repository and place compile.py in the directory of the C/C++ project that you would like to compile and run. In compile.py edit the following as needed:

```python
compiler = 'g++' # g++ for C++, gcc for C
file_to_compile = 'example.cpp' 
libraries_to_link = ['curl', 'jsoncpp'] # add any required libraries here, if none then leave as []
```

Run compile.py in Linux terminal in the directory of your project:
```
cd /your/project/directory
python3 compile.py
```
Press the "enter" key when you're ready to compile and run your project. You can keep this script running in the background while you work on your projects and use it to re-compile and run as needed. Any changes in compile.py will require you to restart compile.py in the terminal. You can stop the script via KeyboardInterrupt by pressing 'ctrl' + 'c' or simply exit out the terminal.

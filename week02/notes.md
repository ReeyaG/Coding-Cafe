1. 'pwd' showed the file location on terminal 
2. ls -a shows all files including the hidden folders whereas ls shows limited files
3. The first column tells if this is a file or a folder
4. a relative path because it does not start from the root directory
5. It moves the file to week 1 and renames the file to old readme
6. /home/reeya/.local/bin:/home/reeya/.nvm/versions/node/v24.18.0/bin:/home/reeya/.espressif/eim:/home/reeya/.local/bin:/home/reeya/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin
(15 in total)

7. /usr/bin/python3

8. The path is not exactly same (friends is: /opt/homebrew/bin/python3.14) this is because we are using different operating systems and he is using homebrew to manage directories and applications on his system. 

9. terminal issues DUMP:  Command 'pyton3' not found, did you mean:
  command 'python3' from deb python3 (3.12.3-0ubuntu2.1)
Try: sudo apt install <deb name>
Basically the error states that there might be a typo and the user should have entered python3, along with that if 
it is not a typo then the user should actually download and install this particular deb.
{Where does PATH come here- basically this typo command does not exist in path {the special folderlist for quick access.}

10. .venv is a hidden folder in the same directory. 

11. "which python3" now shows that the python being used exists in the same directory as the virtual environment (inside the box). Instead of being fetched from path. 

12. activate enabled the virtual environment which allows me to seggregate and work on this project in isolation with my computer and any other projects that could be simuntanously being used. 

13. the following dependencies were installed: 
Package           Version
----------------- -----------
colorama          0.4.6
colorlog          6.12.0
colormap          1.3.0
contourpy         1.3.3
cycler            0.12.1
easydev           0.14.0
fonttools         4.63.0
Jinja2            3.1.6
kiwisolver        1.5.0
line_profiler     5.0.2
MarkupSafe        3.0.3
matplotlib        3.11.1
numpy             2.5.2
packaging         26.3
pandas            3.0.5
pexpect           4.9.0
pillow            12.3.0
platformdirs      4.11.4
ptyprocess        0.7.0
pyparsing         3.3.2
python-dateutil   2.9.0.post0
reports           0.4.1
six               1.17.0
typing_extensions 4.16.0 

earlier it only contained pip with version 24.0

14. Python3 points to the PATH location, same as earlier. 

15. ls -h converts the storage representation which is generally stored in bytes to the closest integer (like in MB or GB so that it could be understood by the user in a more effective manner. 

16. ctrl + C kills the current running program and ctrl + D closes python (like exits from it)

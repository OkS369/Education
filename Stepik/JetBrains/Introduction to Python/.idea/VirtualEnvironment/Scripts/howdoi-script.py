#!"C:\Users\OkS\PycharmProjects\Introduction to Python\.idea\VirtualEnvironment\Scripts\python.exe"
# -*- coding: utf-8 -*-
# EASY-INSTALL-ENTRY-SCRIPT: 'howdoi==1.2.1','console_scripts','howdoi'
__requires__ = 'howdoi==1.2.1'
import re
import sys

from howdoi.howdoi import command_line_runner

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(command_line_runner())
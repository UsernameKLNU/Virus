import colorama
import sys
import platform
import os

def MakeError(error_show, exit_num):
    print(colorama.Fore.RED + error_show + colorama.Fore.RESET)
    sys.exit(exit_num)
    # MakeError("""
    # Traceback (most recent call last):
    #   File "文件路径", line 行数, in <module>
    #     代码块
    # 错误的Exception: 详细错误
    # """, 0xffffffff)

def MakeErrorButDoNotExit(error_show):
    print(colorama.Fore.RED + error_show + colorama.Fore.RESET)
    # MakeError("""
    # Traceback (most recent call last):
    #   File "文件路径", line 行数, in <module>
    #     代码块
    # 错误的Exception: 详细错误
    # """)

def TestPlatform():
    print("关于 Virus")
    print(colorama.Fore.LIGHTBLUE_EX)
    print("Python 版本：" + platform.python_version())

    print("系统：" + platform.platform())

    print("处理器：" + platform.processor())

    print("Virus 版本：" + "1.0.0")
    print(colorama.Fore.RESET)

TestPlatform()

input("确定启动病毒 Virus 1.0.0 吗？ >")
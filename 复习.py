# import time
#
# 时间格式之间的转换
#
# 时间戳----》结构化时间----》格式化时间
# t1 = time.time()
# t2 = time.localtime(t1)
# t3 = time.strftime('%Y-%m-%d %X', t2)
# print(t1)
# print(t2)
# print(t3)
# #
#
# 格式化的时间转换成时间戳
# t1 = time.strptime('2020-07-30 14:42:06', '%Y-%m-%d %X')
# t2 = time.mktime(t1)
# print(t1)
# print(t2)
#
#
# print(time.localtime().tm_year)
#
#
# import datetime
#
# t = datetime.datetime.now()
# print(t)
# 转换时间戳为格式化时间
# print(datetime.datetime.fromtimestamp(time.time()))
# t1 = datetime.datetime.now() - datetime.timedelta(days=3)
# print(t1)
# 直接修改时间
# print(datetime.datetime.now().replace(year=2025))
#
# """
# %a  语言环境的缩写工作日名称。
#
# %A  语言环境的完整工作日名称。
#
# %b  语言环境的缩写月份名称。
#
# %B  地区的完整月份名称。
#
# %c  语言环境的适当日期和时间表示。
#
# 以十进制数字[01,31]表示的月份的日期  %d。
#
# %H  小时(24小时时钟)作为十进制数[00,23]。
#
# %I  小时(12小时时钟)作为十进制数[01,12]。
#
# %j  一年中的一天，以十进制数[001366]表示。
#
# %m  月，以十进制数字[01,12]表示。
#
# %M  分钟作为小数[00,59]。
#
# %p  语言环境相当于AM或PM。(1)
#
# %S  秒，表示十进制数[00,61]。(2)
#
# %U  一年的周数(星期日是一周的第一天)，以十进制数字[00,53]表示。新年第一个星期日之前的所有日子都被认为是在第0周。(3)
#
# %w  以小数形式表示的工作日[0(星期日)，6]。
#
# 某年的周数(星期一是一周的第一天)，以十进制数字[00,53]表示。新年第一个星期一之前的所有日子都被认为是在第0周。(3)
#
# %x  地区的适当日期表示。
#
# %X  地区的适当时间表示。
#
# %y  不含世纪的年份作为十进制数[00,99]。
#
# %Y  年，以世纪作为十进制数。
#
# %z  时区偏移，表示与UTC/GMT的正或负时差，形式为+HHMM或-HHMM，其中H表示十进制小时数，M表示十进制分钟数[-23:59，+23:59]。
#
# %Z  时区名称(如果不存在时区，则无字符)。
#
# 文字“%%”字符。
# """
#
#
# import random
#
# print(random.random())  # 0-1之间的小数
# print(random.randint(1, 3))  # 1、2、3随机一个数
# print(random.choice([1, 2, 3, 4]))  # 列表里随机一个值
# print(random.sample([1, 2, 3, 4, 5], 2))  # 指定随机个数
# print(random.uniform(1, 3))  # 1-3之间的小数
# l = [1, 3, 5, 7]
# random.shuffle(l)
# print(l)
#
#
# def mk_code(n):
#     res = ''
#     for i in range(n):
#         num = str(random.randint(0, 9))
#         alp = chr(random.randint(65, 90))
#         res += random.choice([num, alp])
#     return res
#
# print(mk_code(6))
#
# import os
#
# print(os.listdir('.'))  # 本层目录
# print(os.listdir('..'))  # 上一层目录
# os.system('cmd')
# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.split(__file__))
# print(os.path.basename(__file__))
# print(os.path.dirname(__file__))
# print(os.path.exists(__file__))
# print(os.path.join(__file__, 'a', 'C://'))
# print(os.path.normpath(os.path.join(__file__, '..', '..')))
# print(os.path.getsize(__file__))
# print(os.stat(__file__))
# print(os.environ)
# """
# os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
# os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
# os.curdir  返回当前目录: ('.')
# os.pardir  获取当前目录的父目录字符串名：('..')
# os.makedirs('dirname1/dirname2')    可生成多层递归目录
# os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
# os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.remove()  删除一个文件
# os.rename("oldname","newname")  重命名文件/目录
# os.stat('path/filename')  获取文件/目录信息
# os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
# os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:
# os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
# os.system("bash command")  运行shell命令，直接显示
# os.environ  获取系统环境变量
# os.path.abspath(path)  返回path规范化的绝对路径
# os.path.split(path)  将path分割成目录和文件名二元组返回
# os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)  如果path是绝对路径，返回True
# os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
# os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
# os.path.getsize(path) 返回path的大小
# """
#
# import subprocess
#
# obj = subprocess.Popen("'pwd'; 'echo 123'; 'dir'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(obj.stdout.read().decode('gbk'))
# print(obj.stderr.read().decode('gbk'))
#
#
# import sys
#
# print(sys.path)
# print(sys.argv)
# f1 = sys.argv[1]
# f2 = sys.argv[2]
#
# print(f1)
# print(f2)
#
#
#

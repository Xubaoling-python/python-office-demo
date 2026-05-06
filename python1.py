'''
第一题
编写一个程序，找到2000-3200中所有被7整除但不能被5整除的所有数字，得到的数字按逗号分割，打印在一行上

'''
# def func1():
#     for i in range(2000,3201):
#         if (i%7==0 and i%5!=0):
#             print(i,end=',') 
        
# f1 =func1()


# join() 是 Python 中字符串处理最常用的方法之一。它的主要作用是将序列（如列表、元组）中的元素以指定的字符连接生成一个新的字符串。
# 基本语法
# 'separator'.join(iterable)
# separator（分隔符）：这是你想要用来连接元素的字符串（可以是空字符串、逗号、空格等）
# iterable（可迭代对象）：要连接的序列，通常是列表、元组。注意：序列中的元素必须都是字符串类型。

# li =[]
# for i in range(2000,3201):
#     if (i%7==0 and i%5!=0):
#         li.append(str(i))
# print(','.join(li))


'''
第二题
编写一个可以计算给定数阶层的程序，结果以逗号分割，打印在一行上
'''
# def func2(n):
#     if n == 0 : return 1
#     if n<=2:
#         return n
#     else:
#         return func2(n-1)*n
# f2 =func2(3)
# print("阶层为:",f2)


'''
第三题
使用给定的整数n，编写程序生成一个包含(i,i*i)的字典，该字典包含从1到n之间的整数(俩者都包含),然后打印字典。
假设向程序提供以下输入：
8 则输出为:{1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64}
'''
# 创建一个空字典
# dic ={}
# def func3(n):
#     for i in range(1,n+1):
#         dic[i] = i*i
#     print("输出结果:",dic)
# f3 = func3(8)


'''
第四题
编写一个程序，该程序接收控制台以逗号分割的数字序列，并生成包含每个数字的列表和元组
如：34岁，67岁，55岁，12日，98年；则输出['34','67','55','33','12','98']('34','67','55','33','12','98')
字符串分割是数据处理最常用的操作之一。主要有三种方式：普通分割 (split)、按行分割 (splitlines) 和 分割并保留分隔符 (partition)
'''
# import re

# text4 = input("请输入数字序列，以逗号隔开:")
# def func4():
#     result1 = re.findall(r"\d+",text4)
#     print("列表：",result1)

#     result2 = tuple(result1)
#     print("元组：",result2)

# f4 = func4()


'''
第五题
定义一个至少有俩个方法的类：getString:从控制台输入获取字符串；二printString：打印大写字母的字符串，并写出简单的测试函数来测试类方法
isupper()：该方法用于检测字符串中所有字母是否都为大写
.upper() 方法转大写
'''
# class StringTool():
#     def __init__(self):
#         self.data = ''
#     # getString:从控制台输入获取字符串
#     def getString(self):
#         self.data = input("请输入内容：")
        
#     def printString(self):
#         print("转换结果：",self.data .upper())

# # 测试函数
# def test_class():
#     # 实例化对象
#     my_tool = StringTool()

#     print("开始测试。。。")

#     # 调用获取字符串的方法
#     my_tool.getString()
#     # 调用打印大写的方法
#     my_tool.printString()

# # ----运行测试----
# if __name__=="__main__":
#     test_class()


'''
第六题
编写一个程序，根据给定的公式计算并打印值。其中，假设C=50，H=30 D是一个变量，他的值应该以逗号分割的序列输入到程序中。
例如：程序输入序列为（以逗号分割）：100，150，180；则程序输出为18，22，24

math 是 Python 的标准内置模块，专门用于处理数学运算
常用常量
math.pi：圆周率 π (3.14159…)
math.e：自然常数 e (2.71828…)
常用函数
math.sqrt(x)：求平方根
math.pow(x, y)：求 x 的 y 次方。返回浮点数    注意：这和内置函数 x ** y 或 pow(x, y) 类似，但 math.pow 总是返回浮点数
math.ceil(x)：向上取整（天花板）。只要有小数，整数位就+1
math.floor(x)：向下取整（地板）。直接舍弃小数位
math.fabs(x)：返回绝对值（浮点数）

列表推导式
int_list = [int(x) for x in str_list]
'''

# import math

# def calculate_values():
#     # 定义常量
#     C = 50
#     H = 30

#     # 获取用户输入的值
#     data = input("用户输入：")
#     str_list = data.split(',')
#     # 遍历列表中的每个元素，将其转为 int
#     int_list = [int(x) for x in str_list]

#     for D in int_list:
#         Q = math.floor(math.sqrt((2*C*D)/H))
        
#         print(Q,end=",")

# # 只有类才需要“实例化”，函数可以直接直接调用
# calculate_values()



'''
第七题
编写一个程序，X Y 作为输出（行数和列数），生成一个二维数组，数组的第i行和第j列的元素值应该是i*j
如：程序输入3，5.则程序输出[[0,0,0,0,0],[1,2,3,4],[0,2,4,6,8]]
'''
# def generate_2d_array(x,y):
#     '''
#     生成一个X行，Y列的二位数组，元素值为i*j
#     '''
#     # 外层循环控制行，内层循环控制列
#     return [[i*j for j in range(y)] for i in range(x)]

# f7 = generate_2d_array(3,5)
# print(f7) 


'''
第八题
编写一个程序，以逗号分隔的单词序列作为输入，按照字母顺序对每个单词进行排序，并通过逗号分隔的序列打印单词
如：with，hello，bag，word；则输出bag，hello，with，world

排序
1、list.sort()方法:原地修改列表，返回None，仅适用于列表
nums = [3, 1, 4, 1, 5]
nums.sort()     
2、sorted()函数:返回一个新列表，原对象不变，适用于可迭代对象（列表，元组，字符串，字典等）
nums = [3, 1, 4, 1, 5]
new_nums = sorted(nums) # 生成新列表

reverse=False：默认值，升序
reverse=True：降序（从大到小）
3、按长度排序 (key=len)
words = ["apple", "cat", "banana", "dog"]
words.sort(key=len)
4、忽略大小写 (key=str.lower)
words = ["Banana", "apple", "Cherry"]
words.sort(key=str.lower)
'''
# def Word():
#     data = input("请输入单词序列，以逗号隔开：")
#     # 将字符串分割成列表
#     data_list = data.split(',') 
#     print(data_list) 
#     sorted_data = sorted(data_list)
#     print(sorted_data)
#     # join(),将列表拼回字符串
#     result = ",".join(sorted_data)
#     print(result)

# def Word1():
#     # 列表推导式
#     data = [x for x in input("请输入：").split(',')]
#     # 排序
#     data.sort(key=str.lower)
#     print(",".join(data))


# # Word()
# Word1()



'''
第九题
编写一个程序，接收一行序列作为输入，并将句子中的所有字符大写后打印
字符串的大小写转换
upper():全转大写
lower():全转小写
capitalize():首字母大写，其余小写
title():每个单词首字母大写
swapcase():大小写互换
'''
# def str_upper():
#     text = input("请输入：")
#     print(text.upper())

# str_upper()



'''
第十题
编写一个程序，以一系列空格分搁的单词作为输入，并在删除所有重复的单词后，按字母顺序排序打印这些单词。
如：hello world and practice makes perfect and hello world again,则输出为 again and hello makes perfect practice world

去重
1、使用set()----推荐，但会顺序会乱
my_list = [1, 2, 3, 2, 1, 4, 5]
# 转换为集合去重，再转回列表
new_list = list(set(my_list))

2、使用 dict.fromkeys() (推荐，保持顺序)
my_list = [1, 2, 3, 2, 1, 4, 5]
# 将列表元素作为字典的键，自动去重并保序
new_list = list(dict.fromkeys(my_list))

'''
# def sort_print():
#     text = [i for i in input("请输入:").split(' ')]
#     # 去重
#     new_text = list(set(text))
#     print(new_text)
#     # 排序
#     new_text.sort()
#     print(" ".join(new_text))

# sort_print()


'''
第十一题
编写一个程序，接受一系列以逗号分割的4位二进制数作为输出，然后检查他们是否可被5整除，可被5整除的数字将以逗号分隔的顺序打印
例如：0100，0011，1010，1001  那么输出的应该是1010

进制转换
1、其他进制 → 十进制（使用 int() 函数）
2、十进制 → 其他进制（使用 bin(), oct(), hex() 函数或格式化字符串）

Python 中的进制前缀约定：
二进制：0b (Binary)
八进制：0o (Octal)
十六进制：0x (Hexadecimal)


join()是字符串（str）对象的一个方法，用于将可迭代对象（如列表、元组、字符串等）中的元素连接成一个新字符串
'''
# def switch():
#     # 存储可被5整除的数字
#     divisible_by_5 = []
#     Binary_str = input("输入以逗号分割的4位二进制数:").split(',')
#     for i in Binary_str:
#         # # 转换为十进制整数（二进制数值）
#         int_Binary = int(i,2)
#         if int_Binary%5 == 0:
#             divisible_by_5.append(i)
#     # 返回以逗号分隔的结果
#     return ','.join(divisible_by_5)

# f11 = switch()
# print(f11)



'''
第十二题
编写一个程序，找到1000到3000之间并且所有位数均为偶数的所有数字，比如2000，2002等；获得的数字都以逗号分割的顺序打印在一行上
字符串的 join() 方法
'separator'.join(iterable)
separator：分隔符字符串（连接时插入到元素中间的内容）
iterable：需要连接的可迭代对象（列表、元组等），其中的元素必须是字符串类型
'''
# li =[]
# def number_print():
#     for i in range(1000,3001):
#         if i//1000%2 == 0 and i//100%10%2 == 0 and i//10%10%2   == 0 and i%10%2 == 0:
#             li.append(str(i))

#     print(','.join(li))

# number_print() 


'''
第十三题
编写一个句子并计算字母和数字的程序。假设程序输入:Hello world!123 则应该输出字母10，数字3

'''
# import re
# def sum_print():
#     text = input("请输入：")
#     result = re.findall(r'[a-zA-Z]',text)
#     print(len(result),end=',')
#     result1 = re.findall(r'\d',text)
#     print(len(result1))

# sum_print()



'''
第十四题
编写一个接收句子的程序，并计算大写字母和小写字母的数量。假设为程序提供了以下输入：Hello world！ 则输出：UPPER CASE 1;LOWER CASE 9

'''
# import re
# def count_str():
#     text = input("请输入：")
#     result = re.findall(r'[A-Z]',text)
#     result1 = re.findall(r'[a-z]',text)
#     print("UPPER CASE",len(result))
#     print("LOWER CASE",len(result1))

# count_str()



'''
第十五题
编写一个程序，计算a+aa+aaa+aaaa的值，给定的数字作为a的值。假设为程序提供了以下输入：9；输出11106

字符串拼接
1、使用+运算符
str1 = "Hello"
str2 = "World"
# 直接拼接
result = str1 + " " + str2

2、使用(*):重复
将字符串重复指定次数  字符串 * 整数
a = "9"
print(a * 3) 
# 输出: 999

3、使用join()方法  -----是字符串
words = ['Python', 'is', 'awesome']
# 用空格连接列表中的元素
sentence = " ".join(words)
print(sentence)  # 输出: Python is awesome
'''
# def sum():  
#     li =[]
#     result = 0
    
#     a =input('请输入：')
#     for i in range(1,5):
#         b= a*i
#         li.append(b)
#     for i in li:
#         result += int(i)
    
#     print(result)
# sum()
# sum()
# def calculate_sum():
#     # 获取用户输入的数字
#     a = input("请输入一个数字: ")
#     total_sum = 0
#     for i in range(1, 5):
#         # 生成字符串形式的数字，如 '9', '99', '999', '9999'
#         num_str = a * i
#         total_sum += int(num_str)
        
#     print(total_sum)

# # 运行程序
# calculate_sum()


'''
第十六题
使用列表推导输出列表中的每个奇数，该列表由一系列逗号分隔的数字输入
如 1,2,3,4,5,6,7,8,9 输出1,3,5,7,9
'''
# def number():
#     data = input("请输入:")
#     result = [i for i in data.split(",") if int(i)%2 != 0]
#     print(",".join(result))

# number()



'''
第十七题
需要编写一个程序，按升序对(名称，年龄，高度)元组进行排序，其中name是字符串，age和score是数字，元组由控制台输入
排序标准
1，根据名称排序
2，然后根据年龄排序
3，然后更具分数排序
如输入元组：Tom，19，80；John，17，91；jony，17，93;Json,21,85

replace() 是 Python 字符串中非常常用的方法，用于将字符串中的旧内容替换为新内容 字符串.replace(旧子串, 新子串, 替换次数)
split() 方法返回的一定是列表.具体来说，它返回的是一个由字符串组成的列表
strip() 是 Python 字符串对象的一个内置方法，主要用于去除字符串开头和结尾的指定字符  string.strip([chars]) 返回一个新字符串，原字符串不会被修改

'''
# def sort_tuples():
#     input_str  = input("请输入")
#     # 数据预处理
#     # 处理用户可能输入的中英文标点符号兼容性
#     # 将中文逗号和分号替换为英文逗号和分号
#     input_str = input_str.replace('，', ',').replace('；', ';')
#     # 先按分号 ';' 切割，得到每一条记录
#     items = input_str.split(';')
#     print("items",items)

#     data_list = []
#     for i in items:
#         # 去除可能存在的空格，防止分割后出现空字符串
#         item = i.strip()
#         if not item:
#             continue
#         # 按逗号分割字段
#         parts = i.split(',')
#         print("parts",parts)

#         if len(parts) ==3:
#             name = parts[0].strip()
#             age = int(parts[1].strip())
#             score = int(parts[2].strip())
#             # 构建元组 (名称, 年龄, 分数)
#             data_list.append((name,age,score))
#             print("data_list",data_list)

#     # 3. 排序
#     # 元组默认的排序规则就是先比第一个，再比第二个，再比第三个，正好符合题目要求
#     sorted_data = sorted(data_list)
#     print(sorted_data)
#     # 4. 输出结果
#     print("排序后的结果：")
#     for item in sorted_data:
#         print(item)


# sort_tuples()


'''
第十八题
使用生成器定义一个类，该生成器可以给定范围0-n之间迭代可被7整除的数字

要使用生成器定义类（通常指让类支持迭代，通过生成器实现迭代逻辑），核心是利用Python的迭代协议：
若类实现了__iter__方法并返回一个迭代器，则该类是可迭代的。而生成器函数（含yield）返回的就是迭代器，
因此可通过在类的__iter__方法中调用生成器，使类具备迭代能力。

自定义迭代器类，核心就是在一个类中实现 迭代器协议，即 __iter__ 和 __next__ 两个魔法方法
'''
# class number_divisible():
#     """初始化：指定范围上限n"""
#     def __init__(self,n):
#         self.n =n
        
#     def __iter__(self):
#         """返回迭代器对象(生成迭代器对象)"""
#         for i in range(self.n+1):
#             if i%7==0:
#                 yield i
    
# func1 = number_divisible(20)
# for num in func1:     # 迭代类实例
#     print(num)      # 输出



'''
第十九题
问题：编写一个程序，来计算每个单词出现的频率，按字母顺序对键进行排序后输出

re.sub 是 Python re 模块中用于替换字符串的函数     re.sub(pattern, repl, string, count=0, flags=0)

输入：New to Python or choosing python 2 and Python 3?Read Python 2 or Python 3.
输出：2：2
3：2
New：1

'''
# import re

# emptyDict1 = {}

# def count_word():
#     text = input("请输入：")
#     result = re.sub(r"[^\w]"," ",text).split(" ")
#     print(result)
#     for i in result:
#         # 去除可能存在的空格，防止分割后出现空字符串
#         item = i.strip()
#         if not item:
#             continue
#         emptyDict1[i] = result.count(i)
#     print(emptyDict1)
    
# count_word()



'''
第二十题
编写一个可以计算数学平方值的方法
提示使用**
lambda是Python中的匿名函数（也称为“lambda表达式”），
用于创建小型、临时的函数对象，无需使用def关键字定义函数名。它通常用于需要函数对象但无需重复调用的场景（如作为参数传递给其他函数）。

lambda 参数列表: 表达式
参数列表：可包含0个或多个参数，用逗号分隔（类似函数的参数）
表达式：函数的返回值（只能是一个表达式，不能包含复杂语句，如循环、多行代码）

'''
# def squ(n):
#     result = n**2
#     print(result)

# squ(5)

# square = lambda x:x**2
# print(square(5))



'''
第二十一题
python又许多内置函数，如果不知道如何使用它，可以在线与阅读文档或者查找一些书籍。请编写一个程序来打印python内置函数文档
例如labs(),int()
提示：内置文档方法是doc

help(函数名):help()是Python内置的交互式帮助工具，可直接显示函数的详细文档（包括参数、返回值、示例等）
函数名.__doc__：每个函数都有一个 __doc__ 属性，存储函数的文档字符串（即函数定义时的注释）
'''
# def print_builtin_doc():
#     func_name = input("请输入内置函数名(如len，int，print等):")
#     try:
#         # 直接使用__builtins__（内置模块，无需导入）
#         func = getattr(__builtins__, func_name)
#         print("\n--- 函数文档 ---")
#         print(func.__doc__)

#     except:
#         # 处理函数不存在的情况
#         print(f"错误：找不到内置函数 '{func_name}'，请检查拼写或确认是否为内置函数。")

# # 运行程序
# if __name__ == "__main__":
#     print_builtin_doc()



'''
第二十二题
问题：定义一个类，它具有类参数相同的实例参数
提示：定义一个实例参数，需要在init方法中添加它，您可以使用构造参数初始化对象，也可以稍后设置该值
'''
# class MyClass():
#     # 类参数（类变量）
#     class_param = "类参数的初始值"
#     def __init__(self):
#         # 实例参数（实例变量），初始值等于类参数的值
#         self.instance_param = MyClass.class_param

# # 测试：创建实例并访问参数
# obj = MyClass()
# print(f"实例参数值: {obj.instance_param}")  # 输出：类参数的初始值
# print(f"类参数值: {MyClass.class_param}")   # 输出：类参数的初始值



'''

第二十三题
定义一个可以计算俩个数之和的函数
提示：定义一个带有俩个数字作为参数的函数。可以在函数中计算并返回值

'''
# def sum_number(a,b):
#     return a+b

# result = sum_number(1,9)
# print(result)



'''
第二十四题
定义一个可以将整数转换字符串并在控制台中打印的函数
使用str()将数字转换成字符串
'''
# def str_num(num):
#     print(type(num))
#     result = str(num)
#     print(type(result))
#     print(result)

# str_num(10)


'''
第二十五题
定义一个函数，它可以接收俩个字符串形式的整数并计算他们的和，然后在控制台中输出
提示：使用int()将数字转换为字符串
'''
# def int_num(a,b):
#     result = int(a) + int(b)
#     print(result)
# int_num("10","5")



'''
第二十六题
定义一个函数，它可以接收俩个字符串作为输入，并将他们连接起来，然后再控制台中输出
提示使用+连接字符串
'''
# def Str_str(a,b):
#     result = a+b
#     print(result)

# Str_str("10","20")


'''
第二十七题
定义一个函数，它可以接收俩个字符串作为输入，并在控制台中以最大长度打印字符串。如果俩个字符串长度相同，则函数应逐行打印所有字符串
提示使用len()函数获取字符串长度
'''
# def str_print(a,b):
#     if len(a)>len(b):
#         print(a)
#     elif len(a) == len(b):
#         print(a)
#         print(b)
#     else:
#         print(b)

# str_print("ABC","AB")
# str_print("ABC","DEF")
# str_print("ABC","ABCD")


'''
第二十八题
定义一个函数。它可以接收一个整数作为输入，如果这个数字是偶数，则输出“它是偶数”，否则输出“它是奇数”
'''
# def check_num(n):
#     if n%2==0:
#         print("它是偶数")
#     else:
#         print("它是奇数")

# check_num(10)



'''
第二十九题
定义一个函数，它可以打印一个字典，其中键是1到3之间的数字（包括在内），值是键的平方
提示使用dict[key] = value 模式将条目放入字典中。
使用**运算符得到一个数字的幂
'''
# def print_dict():
#     dict1 = {}
#     for i in range(1,4):
#         dict1[i]=i**2
#     print(dict1)

# print_dict()



'''
第三十四题
定义一个函数，它可以生成一个列表，其中的值是1-20之间的数的平方，然后函数需要打印列表中的前5个元素。
使用**运算符得到一个数字的幂。对循环使用range(),使用list.append()向列表中添加值，使用[n1:n2]对列表进行切片
'''
# def print_list():
#     # 创建一个空元组
#     li =[]
#     for i in range(1,21):
#         li.append(i**2)
#     print(li)
#     print("列表中前5个值:",li[0:5])
#     print("列表中后5个值:",li[-5:])
#     print("列表中除前5个值后,所有的值:",li[5:])

#     # 5. 使用 tuple() 将列表转换为元组
#     result_tuple = tuple(li)
    
#     # 6. 打印结果
#     print("使用tuple()从列表中获取一个元素：",result_tuple[0])

# print_list()


'''
第三十八题
对于给定的元组(1,2,3,4,5,6,7,8,9,10),编写一个程序，在一行中输出前半部分值，在一行中输出后半部分值
使用[n1:n2]表示从元组中获取切片
'''
# def print_tuple():
#     tuple1 = (1,2,3,4,5,6,7,8,9,10) 
#     print(type(len(tuple1)/2))
#     print(tuple1[0:int(len(tuple1)/2)])
#     print(tuple1[int(len(tuple1)/2):])

# print_tuple()


'''
第三十九题
编写程序生成并输出另一个元组，其值是给定元组(1,2,3,4,5,6,7,8,9,10)中的偶数
使用for循环来迭代元组，使用tuple()从列表中生成一个tuple
'''
# tuple1 = (1,2,3,4,5,6,7,8,9,10)
# def print_tuple():
#     li = []
#     for i in tuple1:
#         if i%2 ==0:
#             li.append(i)

#     print(tuple(li))

# print_tuple()


'''
第四十二题
编写一个程序，可以使用map()构造一个列表，其中的元素是[1,2,3,4,5,6,7,8,9,10]中元素的平方
提示：使用map()生成列表。使用lambda定义匿名函数
lambda 参数列表: 表达式
map() 是 Python 内置的一个高阶函数，它用于将一个函数应用到一个或多个可迭代对象（如列表、元组）的每一个元素上，并返回一个新的迭代器
map(function, iterable, ...)
function：函数。这是你要对每个元素执行的操作。
iterable：可迭代对象。如列表、元组、字符串等

'''
# li = [1,2,3,4,5,6,7,8,9,10]
# # 使用 lambda 表达式直接定义平方逻辑
# squares = list(map(lambda x: x ** 2, li))
# print(squares)



'''
第四十三题
编写一个程序，它可以用map()和filter()生成一个列表，其中的元素是[1,2,3,4,5,6,7,8,9,10]中的偶数平方
提示：使用map()生成列表。使用filter()来过滤列表中的元素。使用lambda定义匿名函数 

filter() 也是 Python 内置的一个高阶函数，它的作用正如其名——过滤。
filter(function, iterable)
function：判断函数。该函数接收一个参数，返回布尔值。
iterable：可迭代对象（列表、元组等）。
返回值：返回一个 filter 对象（迭代器），需要用 list() 转换才能看到结果
它会遍历可迭代对象（如列表）中的元素，将元素传入一个函数进行判断：
如果函数返回 True，保留该元素。
如果函数返回 False，丢弃该元素。
'''
# li = [1,2,3,4,5,6,7,8,9,10]
# li1 = list(filter(lambda i:i%2 ==0,li))
# print(li1)
# squares_numbers = list(map(lambda x: x ** 2, li1))
# print(squares_numbers)



'''
第四十四题
编写一个程序，它可以使用map()生成一个列表，其中的元素是1-20之间的数的平方
使用map()生成列表。使用lambda定义匿名函数
'''
# squares_numbers = list(map(lambda x:x**2,range(1,21)))
# print(squares_numbers)



'''
第四十五题
定义一个名为American的类，她有一个名为printNationality的静态方法
提示：使用@staticnthod装饰器来定义类的静态方法
第四十六题
问题:定义一个名为American的类及其子类NewYorker。
提示:使用类子类(ParentClass)来定义子类。
super() 是 Python 中用于调用**父类（超类）**方法的一个内置函数。它最主要的作用是解决子类重写父类方法后，如何复用父类代码的问题
'''
# class American():
#     @staticmethod
#     def printNationality():
#         print("这是一个静态方法")

#     def __init__(self,name):
#         self.name =name
    
#     def greet(self):
#         print(f"Hello, I am {self.name} from America.")

# # 子类NewYorker
# class NewYorker(American):
#     def __init__(self, name,district):
#         # 没有使用 super）：
#         # 如果子类定义了 __init__，父类的 __init__ 就不会被自动调用，导致父类的属性丢失
#         # 调用父类的构造方法初始化 name
#         super().__init__(name)
#         self.district = district

#     # 子类特有的方法
#     def show_district(self):
#         print(f"I live in {self.district}, New York.")


# # # 静态方法可以直接通过类名调用，不需要实例化
# American.printNationality()  # 通过类名调用

# # 也可以通过实例调用   不推荐
# obj =American()
# obj.printNationality()

# # 创建 NewYorker 实例
# ny_resident = NewYorker("John", "Manhattan")

# # 调用从父类继承的方法
# ny_resident.greet()

# # 调用子类自己的方法
# ny_resident.show_district()

# # 验证继承关系
# print(isinstance(ny_resident, American))  # 输出: True


'''
第四十七题
定义一个名为Circle的类，可以用半径来构造。Circle类有一个可以计算面积的方法
第四十八题
定义一个名为Rectangle的类，它可以由长度和宽度构造。矩形类有一个方法可以计算面积。
'''
# import math
# class Circle():
#     def __init__(self,r):
#         self.r = r
#     def area(self):
#         return math.pi*(self.r**2)
    
# class Rectangle(Circle):
#     def __init__(self,l,w):
#         self.l = l
#         self.w = w
#     def area(self):
#         return self.l*self.w
    
    

# cir = Circle(5)
# cir1 = cir.area()
# print(f"圆面积为:",cir1)
# #
# Rec = Rectangle(5,10)
# rec = Rec.area()
# print(f"长方形面积为:",rec)


'''
第五十一题
编写一个函数来计算5/0，并使用try/except来捕获异常

'''
# def Error(n):
#     try:

#         result = 5/n
#     except:
#         print("捕获异常")
# Error(0)



'''
第五十三题
问题:假设我们有一些’username@companyname.com格式的电子邮件地址，请编写程序打印给定电子邮件地址的用户名，用户名和公司名都只由字母组成。
示例:如果下面的电子邮件地址作为程序的输入:john@go0gle.com.
那么，程序的输出应该是:john
在向问题提供输入数据的情况下，应该假定它是控制台输入。
'''
# def Emile_name():
#     text = input("请输入邮箱:")
#     text_li = text.split("@")
#     print(text_li[0])

# Emile_name()


'''
第五十四题
#问题:假设我们有一些“username@companyname.com”格式的电子邮件地址，请编写程序打印给定的电子邮件地址的公司名称:用户名和公司名都只由字母组成。
示例:如果下面的电子邮件地址作为程序的输入:john@go0gle.com那么，程序的输出应该是:g00gle
在向问题提供输入数据的情况下，应该假定它是控制台输入。
'''
# import re

# def Company_name():
#     while True:
#         text = input("请输入邮箱:")
#         # 仅匹配纯字母的邮箱，如 john@google.com
#         pattern = r'^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$'

#         if re.match(pattern,text):
#             print("邮箱格式正确")
#             text_li = text.split("@")[1]
#             print(text_li.split(".")[0])
#             break
#         else:
#             print("错误：邮箱格式不正确！")

# Company_name()
# import re

# def extract_company(email):
#     # 定义正则表达式
#     # ^(\w+)      : 匹配开头用户名 (第1组)
#     # @           : 匹配 @ 符号
#     # (\w+)       : 匹配公司名称 (第2组，这是我们想要的)
#     # \.com$      : 匹配结尾的 .com
#     pattern = r"^(\w+)@(\w+)\.com$"
    
#     result = re.match(pattern, email)
    
#     if result:
#         # group(2) 对应正则中第二个括号内的内容，即公司名称
#         return result.group(2)
#     else:
#         return "格式不匹配"

# # 测试示例
# email_address = "john@g00gle.com"
# company_name = extract_company(email_address)
# print(company_name)



'''
第五十五题
问题:编写一个程序，接收一个由空格分隔的单词序列作为输入，打印只由数字组成的单词。
示例:如果下面的单词作为程序的输入:2cats and 3dogs;
那么，程序的输出应该是:[‘2’，’3’]在向问题提供输入数据的情况下，应该假定它是控制台输入。

re.findall(pattern, string)
特点：扫描整个字符串，找到所有匹配项。
返回：返回一个列表，元素是匹配到的字符串（如果有分组，则是分组的元组列表）
'''
# import re

# def str_print():
#     text = input("输入:")
#     number = re.findall(r"\d",text)
#     print(number)

# str_print()



'''
python中的解码与编码
编码与解码是处理文本数据的核心概念，主要涉及到 str (字符串) 和 bytes (字节) 两种数据类型的相互转换
编码: 把人类能看懂的 字符串 变成计算机能存储/传输的 字节。
解码: 把计算机存储的 字节 变成人类能看懂的 字符串


Python 提供了两个内置方法来处理这个过程
A. 编码 (encode)  将 str 转换为 bytes
语法：字符串对象.encode(encoding='编码格式')
B. 解码 (decode)  将 bytes 转换为 str
语法：字节对象.decode(encoding='编码格式')

'''
# s = "你好"
# # 默认使用 UTF-8 编码
# b1 = s.encode() 
# print(b1)  # 输出: b'\xe4\xbd\xa0\xe5\xa5\xbd'

# b = b'\xe4\xbd\xa0\xe5\xa5\xbd' # 这是 UTF-8 编码的“你好”

# # 必须使用正确的编码格式解码
# s = b.decode("utf-8")
# print(s)  # 输出: 你好



'''
第五十九题
问题:写一个程序来计算1/2+2/3+3/4+......+n/(n+1)。示例:如果下面的n作为程序的输入:5;那么，程序的输出应该是:3.55;
'''
# def add(n):
#     if n == 1:
#         return 1/2
#     else:
#         return n/(n+1)+add(n-1)
# result = add(5)
# print(f"{result:.2f}")



'''
第六十题
问题:编写程序计算:当n>0和F(0)=0时，F(n)=F(n-1)+100通过控制台输入一个给定的n (n>0)。示例:如果下面的n作为程序的输入:5，
那么，程序的输出应该是:500;
'''
# def F(n):
#     if n==0:
#         return 0
#     else:
#         return F(n-1)+100
    
# result = F(5)
# print(result)



'''
第六十一题
问题:斐波那契数列的计算公式如下:如果n=0.f(1)=0:如果=1,f(1)=1:如果n>1,f(n)=f(n-1)+f(n-2);请编写一个程序，在控制台输入给定n的情况下计
算f(n)的值。
示例:如果下面的n作为程序的输入:7;
那么，程序的输出应该是:13;
'''
# def Fibo(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return Fibo(n-1)+Fibo(n-2)
# result = Fibo(7)
# print(result)



'''
第六十二题
问题:请使用generator编写一个程序，当n由控制台输入时，以逗号分隔的形式输出0和n之间的偶数;示例:如果下面的n作为程序的输入10:
那么，程序的输出应该是:0,2,4,6,8,10;
'''
# def generator(n):
#     for i in range(n+1):
#         if i%2==0:
#             yield i

# # 功能：调用生成器函数 generator(10)，创建一个生成器对象 gen。
# # 细节：此时 gen 还没有执行循环，只是“准备”生成值（生成器是“惰性”的，不会立即计算所有结果）
# gen = generator(10)
# # 输出：会显示生成器对象的内存地址，例如 <generator object generator at 0x0000012345678900>。
# # 含义：gen 是一个生成器，不是具体的值列表，需要通过迭代（如 for 循环或 list()）才能获取其中的值。
# print(gen)
# even_numbers = list(map(str, gen))  # 将生成器的每个数字转为字符串
# print(even_numbers)
# print(",".join(even_numbers))



'''
第六十三题
问题:请编写一个生成器程序，以逗号分隔的形式输出0到n之间可以被5和7整除的数字，而n是通过控制台输入的。
示例:如果下面的n作为程序的输入:100:
那么，程序的输出应该是:0,35,70;
'''
# def generator(n):
#     for i in range(n+1):
#         if i%5==0 and i%7==0:
#             yield i

# n=int(input("输入n："))
# gen = generator(n)
# # map(str, gen)：map() 是Python内置函数，作用是将 str 函数（将数字转为字符串）应用到 gen 的每个元素上。map() 返回一个map对象（迭代器）。
# # list(...)：将 map 对象转换为列表，此时生成器被迭代一次，所有偶数被取出并转为字符串，例如 ['0', '2', '4', '6', '8', '10']。
# even_numbers =list(map(str, gen)) 
# print(",".join(even_numbers))


'''
第六十四题
#问题:请写assert语句来验证列表[2,4,6,8]中的每个数字都是偶数。
提示:使用“断言表达式”进行断言。

assert 条件, "错误信息（可选）"
条件：需要检查的逻辑表达式（如x > 0）。
错误信息：当条件为False时，抛出的异常消息（可选，不写则默认为空）
'''
# li = [2,4,6,8,9]
# def assert_number():
#     for i in li:
#         assert i%2==0,f"列表中的元素 {i} 不是偶数"
# assert_number()



'''
第六十五题
#问题:请编写一个程序，从控制台接收基本数学表达式，并输出计算结果。
#示例:如果下面的字符串作为程序的输入:35+3;那么，程序的输出应该是:38;

eval() 是 Python 的内置函数，用于执行字符串形式的 Python 表达式，并返回表达式的计算结果.
适用于数学计算、变量访问、函数调用等场景。

eval(expression, globals=None, locals=None)
expression：必选参数，字符串形式的 Python 表达式（如 "2 + 3"、"len([1,2,3])"）
globals 和 locals：可选参数，用于指定全局和局部命名空间（通常用默认值即可）。

'''
# import re
# def num():
#     data = input("输入内容:")
#     pattern = r"(\d+)([\+\-\*/])(\d+)"
#     match = re.match(pattern, data)
#     num1 = match.group(1)
#     print(type(num1))
#     operator  = match.group(2)
#     num2 = match.group(3)

#     if operator =='+':
#         return int(num1)+int(num2)
#     elif operator == '-':
#         return int(num1)-int(num2)
#     elif operator == '*':
#         return int(num1)*int(num2)
#     elif operator == '/':
#         if int(num2) == 0:
#             return "Error: Division by zero"
#         return int(num1) / int(num2)
    
# result = num()
# print(result)


# expr =input("请输入数学表达式:")
# print(eval(expr))  # 解释表达式，输出结果


'''
第六十六题
随机生成1，100内的一个整数
random模块是Python标准库中用于生成伪随机数的模块，常用于模拟随机事件、随机抽样、数据打乱等场景
第六十八
问题:请编写一个程序输出0和10之间的随机偶数使用随机模块和列表理解。
第六十九题
问题:请编写一个程序输出一个随机数，它可以被5和7整除，在0和10之间，使用随机模块和列表理解。

(1) random.random() 功能：生成0到1之间的浮点数（含0，不含1）
(2) random.randint(a, b) 功能：生成a到b之间的整数（含a和b）
(3) random.choice(seq) 功能：从序列（列表、元组、字符串等）中随机选择一个元素
(4) random.sample(population, k) 功能：从population中随机选择k个不重复的元素（返回新列表）。
(5) random.shuffle(x) 功能：将序列x随机打乱顺序（原地操作，不返回新列表）。
(6) random.uniform(a, b) 功能：生成a到b之间的浮点数（含a和b，具体实现可能因版本略有差异）
(7) random.randrange(start, stop[, step]) 功能：从range(start, stop, step)中随机选择一个数（类似于randint但支持步长）
'''
# import random
# result = random.randint(1,100)
# print(result)
# result1 = random.choice([i for i in range(0,11) if i%2==0])
# print(result1)



'''
第六十九题
问题:请编写一个程序输出一个随机数，它可以被5和7整除，在0和10之间，使用随机模块和列表理解。
'''







    





#coding=utf-8
# from module1 import printer
# printer('hello world!')

import module1
module1.printer('hello world!')
module1.spam=2
print module1.__dict__.keys()

# #import只执行一次
# import module1
# print module1.spam
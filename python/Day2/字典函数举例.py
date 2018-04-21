#encoding=UTF-8
stu={'name':'job','ages':'20'}
for k in stu.keys():
	print(k)
for v in stu.values():
	print(v)
print('='*30)
#迭代字典的常用方法
for item in stu.items():
	print(item)
	print('key为%s,value为%s'%item)
#判断某个key在字典中
print('='*30)
key='name'
if key in stu:
	print('%s在字典中'%key)
if stu.has_key(key):
	print('%s在字典中'%key)

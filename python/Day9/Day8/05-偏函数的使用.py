def showargs(*args,**kwargs):
	print(args)
	print(kwargs)

import functools
p1=functools.partial(showargs,1,2,3)
p1()
p1(a='job',b='jack')
p1(a='shanghai',b='beijing')


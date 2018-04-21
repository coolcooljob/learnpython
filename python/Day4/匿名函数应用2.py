stus=[{'name':'job','age':'20'},{'name':'laoli','age':'23'}]
a=[123,456,67,789]
#a.sort(reverse=True)
#print(a)
stus.sort(key=lambda x:x['age'],reverse=True)
print(stus)


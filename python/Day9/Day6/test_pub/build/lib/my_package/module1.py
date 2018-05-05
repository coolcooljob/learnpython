def isnull(str):
	if not str:
		return True
	elif str.strip()=='':
		return True
	else:
		return False

#测试代码,只要模块被导入，就调用，必须加一个判断
if __name__=='__main__':    #由python解释器主动执行，该模块代码为了测试
	print(isnull('1234'))

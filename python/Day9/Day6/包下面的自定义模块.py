 #此目录下面没有直接的module1模块,而是将此模块放入my_package包下面，所以导入方式要有所变化
import my_package.module1    
print(my_package.module1.isnull('123'))

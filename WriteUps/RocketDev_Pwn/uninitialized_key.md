# uninitialized key

## 文件分析

下载`uninitialized_key`, 保护全开  
ghidra分析为64位程序

## 逆向

该程序存在两个重要函数：`get_name`和`get_key`  
在后者中，只要key==114514 ~~怎么又是这么臭的数字~~ ，就可以cat flag，但是%5d的截断使输入该数成为不可能  
在前者中，数字输入没有限制，通过gdb调试发现，第一次输入数字后会push到esp上  
只要第二次输入时输入无效输入，就可以保留esp的值在`key`上 

## EXPLOIT

nc localhost 37713  
*114514*  
*asdfasdf*

> 斜体代表输入，正体代表命令

Done.

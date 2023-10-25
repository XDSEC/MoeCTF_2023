# 前置软件
读代码可以使用`objdump -d`或者`ghidra`，调试我使用`pwndbg`

在比赛中我没有直接使用常见的[pwntools](https://github.com/Gallopsled/pwntools)，而是使用了[pwncli](https://github.com/RoderickChan/pwncli)，感觉虽然还未很成熟，但是比直接使用`pwntools`来说方便许多
**注意： pwncli可能会替换~/.gdbinit，其内置的备份机制存在bug，导致可能会无法恢复，已知pypi上的版本存在此问题，所以请不要从pypi上安装**
## 如何使用pwncli/我的exp.py脚本
- 打本地
```shell
./exp.py de ./format_level3 -nl -u -G pwndbg
```
- 打远程
```shell
./exp.py re ./format_level3 localhost:1236
```
更详细的用法请查阅[GitHub](https://github.com/RoderickChan/pwncli)或者使用
```shell
./exp.py -h
./exp.py de -h
./exp.py re -h
```
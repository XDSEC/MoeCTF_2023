# fd

## 文件分析

下载`fd`, 保护全开  
~~ghidra分析为??位程序~~

## 逆向

经过分析，没有漏洞可钻，自然也就没必要知道是几位的程序了

这道题突破口在于输入匹配的File Discriptor，直接拿到flag  
测试可知，第一次打开文件，fd永远是3  
由于`fd`被关闭，只要计算`new_fd`即可

## EXPLOIT

```python
print(3 << 2 | 666)
```

nc连接，输入该数即拿到flag

Done.

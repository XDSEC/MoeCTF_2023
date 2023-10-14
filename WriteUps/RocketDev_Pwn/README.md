# moectf 2023 Writeup

Author: [@RocketMaDev](https://github.com/RocketMaDev)

这些wp建议读者先有做出ret2txt的能力再看，图片极少，建议自行调试，更有助于理解

## 题目索引

以下题目按题表排序，用L?标注难度，越高越难

1. [Pwn入门指北](./前两题.md) (前两题同一个markdown) L0
2. [test_nc](./前两题.md) L1
3. [baby_calculator](./BabyCalculator.md) L1
4. [fd](./fd.md) L1
5. [int_overflow](./IntOverflow.md) L1
6. [ret2text_32](./return2text_32.md) L1
7. [ret2text_64](./return2text_64.md) L1
8. [shellcode_level0](./shellcode_level0.md) L1
9. [shellcode_level1](./shellcode_level1.md) L1
10. [uninitialized_key](./uninitialized_key.md) L1
11. [format_level0](./format_level0.md) <font color=CadetBlue>L2</font>
12. [PIE_enabled](./pie_enabled.md) <font color=CadetBlue>L2</font>
13. [ret2libc](./ret2libc.md) <font color=CadetBlue>L2</font>
14. [ret2syscall](./ret2syscall.md) <font color=CadetBlue>L2</font>
15. [shellcode_level2](./shellcode_level2.md) <font color=CadetBlue>L2</font>
16. [uninitialized_key_plus](./uninitialized_key_plus.md) <font color=CadetBlue>L2</font>
17. [format_level1](./format_level1.md) <font color=Orange>L3</font>
18. [little_canary](./little_canary.md) <font color=CadetBlue>L2</font>
19. [rePWNse](./rePWNse.md) L1
20. [shellcode_level3](./shellcode_level3.md) <font color=CadetBlue>L2</font>
21. [changeable_shellcode](./changeable_shellcode.md) <font color=Red>L4</font>
22. [format_level2](./format_level2.md) <font color=Red>L4</font>
23. [feedback](./feedback.md) <font color=Orchid>L5</font>
24. [format_level3](./format_level3.md) <font color=Orchid>L5</font>

## Copyright

Distributed under CC BY-NC 4.0  
Copyright RocketDev 2023

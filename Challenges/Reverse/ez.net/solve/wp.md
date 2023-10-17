整完以后发现好像有点太过阴间了（
简单分析可以发现最后验证的逻辑是在`KoitoMagicalShop`里面，其中`GetNextSpellcard`是我随手写的一个流密码（
所以解题的关键就在于，找到这个流密码的key（8字节），静态分析可以判断得到catfood的返回值，然后就是10008个重写的入口，一个一个试一试（用反射直接获取到所有重写，然后分别调用
flag的长度是72，复制一个`IsRealFlag`方法，参数中的flag用全0替代，如果密钥正确的话，`NoMagicalFlag`就是flag
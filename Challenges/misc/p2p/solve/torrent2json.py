# 直接找的 https://blog.csdn.net/m0_50910065/article/details/126951147
import json
 
# 二话不说，先读取
file="segments.torrent"
 
if file[0] in ["'",'"']:
    file=file[1:-1]
f=open(file,'rb')
s=f.read()
f.close()
 
# %%
# 由基本数据类型得到以下一些标识符：
sign_num = b'0123456789' # 表示数字
sign_str = b':' # 字符串
sign_int = b'i' # 整数
sign_list= b'l' # 列表
sign_dict= b'd' # 字典
sign_end = b'e' # 整数和列表和字典的结尾
 
 
# %%
# 提取字符串
 
# 这个函数用来获取字符串的长度
def len_str(s,i, start_safe=0):
    '''### 获取字符串/字节串的长度
    #### input:
    - s: 整体的字符串
    - i: 标识符 ":" 的位置
    - start_safe: 从此位置开始往后计算，此前的屏蔽掉
    #### return: 字符串的长度
    '''
    num=b''
    j=0
    while s[i-j-1:i-j] in sign_num and i-j>start_safe:
        num = s[i-j-1:i-j]+num
        j+=1
 
    if len(num)>0:
        return int(num)
    else:
        return 0
 
# %%
# 将里面的字符串全部提取
# 将所有的字符串全部转化为指定的字符：s
i=0
s_del_str = s
 
length_del=0
end_str=0
len_str_lis=[]
str_lis = []
 
while i<len(s):
    if s[i:i+1]==sign_str:
        length=len_str(s,i, start_safe=end_str)
        len_str_lis.append(length)
 
        if length>0:
            # print(s[i+1:i+length+1])
            str_lis.append(s[i+1:i+length+1])
            s_del_str = s_del_str[:i-len(str(length))-length_del]+ b's' +s_del_str[i+1+length-length_del:]
            length_del += len(str(length))+length
            end_str = i+length+1
        
        i+=length
    i+=1
 
 
# %%
# 提取数字
def len_int(s,i):
    j=1
    while s[i+j:i+j+1] in sign_num and i+j<len(s):
        j+=1
 
    return j-1
 
i=0
s_del_int=s_del_str
length_del_int=0
int_lis=[]
 
while i<len(s_del_str):
    if s_del_str[i:i+1] == sign_int:
        length=len_int(s_del_str,i)
        # print(s_del_str[i+1:i+1+length])
        int_lis.append(int(s_del_str[i+1:i+1+length]))
        s_del_int = s_del_int[:i-length_del_int]+ b'i' +s_del_int[i+2+length-length_del_int:]
 
        i+=length
        length_del_int+=length+1
    i+=1
 
 
# %%
# 处理列表和字典
s_list_dict=s_del_int.replace(b'l',b'[').replace(b'd',b'{')
s_del_list_dict=s_list_dict
 
lis_sign_near=[]
i=0
while i<len(s_list_dict):
    if s_list_dict[i:i+1]==b'[':
        lis_sign_near.append(b']')
    elif s_list_dict[i:i+1]==b'{':
        lis_sign_near.append(b'}')
    
    elif s_list_dict[i:i+1]==b'e':
        s_del_list_dict=s_del_list_dict[:i]+lis_sign_near[-1]+s_del_list_dict[i+1:]
        lis_sign_near=lis_sign_near[:-1]
    
    i+=1
 
s_del_list_dict = s_del_list_dict.replace(b'[s]',b's')
 
# %%
# 相当难搞
i=0
j=0
sign_lis=False
k_lis=[]
 
data=s_del_list_dict
lis_sign_near=[]
while i<len(s_del_list_dict):
    if s_del_list_dict[i:i+1] in [b's',b'i'] and s_del_list_dict[i+1:i+2] not in [b']',b'}']:
        j+=1
        if not sign_lis:
            k_lis[-1]+=1
            if k_lis[-1]%2==1:
                data=data[:i+j]+b':'+data[i+j:]
            else:
                data=data[:i+j]+b','+data[i+j:]
        else:
            data=data[:i+j]+b','+data[i+j:]
    
    elif s_del_list_dict[i:i+1] in [b'[',b'{']:
        lis_sign_near.append(s_del_list_dict[i:i+1])
        if s_del_list_dict[i:i+1]==b'{':
            k_lis.append(0)
            
    elif s_del_list_dict[i:i+1] in [b']',b'}']:
        lis_sign_near=lis_sign_near[:-1]
        j+=1
        data=data[:i+j]+b','+data[i+j:]
 
        if s_del_list_dict[i:i+1]==b'}' and len(k_lis)>0:
            k_lis=k_lis[:-1]
        
        if len(lis_sign_near)>0:
            if lis_sign_near[-1]==b'[':
                sign_lis=True
            else:
                sign_lis=False
                k_lis[-1]+=1
 
    if len(lis_sign_near)>0:
        if lis_sign_near[-1]==b'[':
            sign_lis=True
        else:
            sign_lis=False
    
    i+=1
    
 
# 最后填充数据
 
data=data.replace(b',]',b']').replace(b',}',b'}')[:-1]
data=data.decode('utf8').replace('s','"temp_str"').replace('i','"temp_int"')
 
# %%
# 填充数据
for i in str_lis:
    if len(i)<100:
        try:
            data=data.replace('temp_str',str(i.decode()), 1)
        except:
            data=data.replace('temp_str',"can't decode", 1)
    else:
        data=data.replace('temp_str','too long', 1)
 
for i in int_lis:
    data=data.replace('temp_int',str(i), 1)
 
 
# 一些意外情况
while '""' in data:
    data=data.replace('""','"')
while '\t' in data:
    data=data.replace('\t','-')
while '\n' in data:
    data=data.replace('\n','-')
 
# %%
# 输出为json
# 这里输出为一种肉眼可见的方便的格式(json)
# 更人性化的输出后续在此基础上自己动手修改
 
try:
    result_json = json.loads(data) # except，主要就是上面那些意外情况
    if 'info' in result_json:
        print('\ninfo:')
        print(json.dumps(result_json['info'], indent=4, ensure_ascii=False))
 
    f=open(file.replace('.torrent','.json'),'w', encoding='utf8')
    f.write(json.dumps(result_json, indent=4, ensure_ascii=False))
    f.close()
 
    input('\n  读取成功\n\n详细信息已保存至同名json文件中')
 
except:
    input('\n  读取失败：字符串转为字典的时候出错\n\n赶紧滚去修bug')
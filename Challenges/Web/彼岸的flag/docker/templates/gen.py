import random
import os

HEAD = open(f'{os.path.dirname(__file__)}/htmlhead', 'r', encoding='utf-8').read()
TAIL = open(f'{os.path.dirname(__file__)}/htmltail', 'r', encoding='utf-8').read()

avatars = ['https://s3.bmp.ovh/imgs/2023/07/19/48313fa50fbb31c1.jpg',
           'https://s3.bmp.ovh/imgs/2023/07/19/c2e2bf051a813b53.png']
admin_ava = 'https://s3.bmp.ovh/imgs/2023/07/19/6d48dd9462903be7.jpg'

data = [
    '师傅带带我！',
    '@[error: can\'t track user]能教我ctf吗？',
    '@[error: can\'t track user]能教我ctf吗？',
    '@[error: can\'t track user]能教我ctf吗？',
    '@[error: can\'t track user]能教我ctf吗？',
    '@[error: can\'t track user]能教我ctf吗？',
    '@[error: can\'t track user]能教我ctf吗？',
    '@[error: can\'t track user]能教我ctf吗？',
    '谔谔',
    '@[error: can\'t track user]能教我ctf吗？',
    '@[error: can\'t track user]能教我ctf吗？',
    '@[error: can\'t track user]能教我ctf吗？',
    '救命',
    'ctf是啥',
    '不会百度吗？= =',
    'QAQ',
    '还是王者好玩，就是一直连跪',
    '原来你也玩( )',
    '原来你也玩( )',
    '原来你也玩( )',
    '都玩是吧',
    '一定是米哈游干的',
    ('notice', '昨天 13:21'),
    '话说比赛啥时候开始',
    ('notice', '昨天 15:14'),
    ('admin', '八月份'),
    ('notice', '昨天17:54'),
    'AK了来水群是吧',
    'AK了来水群是吧',
    '回复："AK了来水群是吧"\n没有',
    '各位大佬，请问有关于RCE的视频推荐嘛',
    '回复："各位大佬，请问有关于RCE的视频推荐嘛"\n推荐视频:崩坏：星穹铁道1.2前瞻',
    ('notice', '昨天19:05'),
    '带带我这只小萌新',
    '带带我',
    '我也想进步',
    '大佬带带我',
    ('admin', '再钓鱼踢了'),
    '我是真菜狗',
    ('admin', '不是说你'),
    ('admin', '老师傅有时间可以看看群里提问，有兴趣就回答一下，但是别在这钓萌新'),
    '云之君明明是学姐，感觉已经被叫了两年学长了',
    '居然是学姐吗',
    '?',
    '?',
    '?',
    '是神仙',
    ('admin', '回复："居然是学姐吗"\n是你跌'),
    ('admin', '我寻思你们平时叫我云又不叫我君'),
    '那以后叫你云nokimi（（（',
    '☁',
    '☁之🍄',
    '吃了就会上天的菌子',
    ('admin', '你说得对'),
    ('admin', '但是shallow难道不可爱吗'),
    '👀',
    '所以真的是学姐吗',
    ('notice', '昨天23:32'),
    '纯萌新，想请教一下，cms识别出来以后有什么用啊',
    '回复："纯萌新，想请教一下，cms识别出来以后有什么用啊"\n找历史漏洞利用或者看看readme的默认密码',
    '看版本有没有历史漏洞或者1day利用？',
    '如果是开源的还可以代码审计',
    '谢谢大佬',
    'web有什么入门指引吗',
    '细化到周的那种',
    '刷题不就好了',
    '感觉刷题和真实渗透有差',
    'ctf纯刷题',
    'src不用刷题',
    '🥲',
    '渗透直接上实操（合法情况下',
    ('notice', '0:53'),
    '<img src="https://s3.bmp.ovh/imgs/2023/07/19/62392b64194e60a4.jpg">',
    ('notice', '2:14'),
    ('notice', f'管理员[error, can\'t track user] 撤回了一条消息<!--经过tracker，破获出内容为{os.getenv("FLAG")}-->'),
    ('notice', '3:51'),
    '?',
    ('notice', '6:43'),
    '起床学习！',
    '学驾照',
    ('notice', '8:21'),
    '纯萌新，想请教一下用搜索引擎搜索ico文件是做什么的啊',
    '?',
    'Ico不是图标吗',
    '谷歌搜图吧',
    '有的资产 ico 可以作为指纹（',
    '回复：<img src="https://s3.bmp.ovh/imgs/2023/07/19/62392b64194e60a4.jpg">\n下面换成1:04将成绝杀',
    '回复："有的资产 ico 可以作为指纹（"\n感谢感谢'
]


def rand_avatar():
    return '''<div class="avatar"><img src="''' + random.choice(avatars) + '''" /></div>'''


def left_bub(content: str):
    h = '''<div class="bubble bubble-left">'''
    t = '''</div>'''
    s = content.replace('\n', '<br/>')
    return h + s + t


def new_left(content: str):
    h = '''<div class="item item-left">'''
    t = '''</div>'''
    return h + rand_avatar() + left_bub(content) + t


def adm_left(content: str):
    h = '''<div class="item item-left">'''
    t = '''</div>'''
    return h + '<div class="avatar"><img src="' + admin_ava \
           + '"></div>' + left_bub(content) + t


def new_notice(content: str):
    h = '''<div class="item item-center"><span>'''
    t = '''</span></div>'''
    return h + content + t


def gen(data: list):
    res = ''

    for info in data:
        if type(info) == str:
            res += new_left(info)
        else:
            if info[0] == 'admin':
                res += adm_left(info[1])
            elif info[0] == 'notice':
                res += new_notice(info[1])
            else:
                raise SyntaxError('格式错误')

    return res


BODY = gen(data)
open(f'{os.path.dirname(__file__)}/ChatLog.html', 'w', encoding='utf-8').write(HEAD + BODY + TAIL)

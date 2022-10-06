import httpx
from nonebot import on_command, on_notice
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Event, PokeNotifyEvent,LuckyKingNotifyEvent,GroupRecallNoticeEvent
import random
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name='戳一戳',
    description='消遣',
    usage='戳一戳地瓜',
    extra={
        'author': 'hamo-reid',
        'menu_template': 'default'
    }
)

a = ['那...那里...那里不能戳...绝对...','嘤嘤嘤,好疼','你再戳，我就把你的作案工具没收了，哼哼~','别戳了别戳了，戳怀孕了',
   '嘤嘤嘤，人家痛痛','我错了我错了，别戳了','桥豆麻袋,别戳老子','手感怎么样','戳够了吗？该学习了','戳什么戳，没戳过吗',
   '你用左手戳的还是右手戳的？','不要啦，别戳啦','给你一拳','再摸就是狗','你这么闲吗？','代码写完了吗？','再戳，怀孕了你负责吗？',
   '爬去学习','你就是sp一个','么么哒','不要这样嘛!','你好讨厌哦!','你好坏哦，欺负人家，哼！','不要酱紫嘛','一天没和你聊天，就觉得哪里不对劲！',
   '快亲亲人家啦!!','不理你了，真讨厌。','人家不要了啦!','你今天有没有想念人家呀!','别这样啦，人家是个女孩子嘛!',
   '(✿◡‿◡)','(*/ω＼*)','つ﹏⊂','ヾ(≧O≦)〃嗷~','(>▽<)，好呀','恶心心','mu--a','可以教我写代码吗','记得按时吃饭哦']

xiuxiu=['喜欢人家就直说啊,我还没说不同意呢~',"撤回了什么让我也康康呗","咦。。。。我看到了","羞羞的东西，被我看到了","怀孕了就直说啊，撤回干嘛","wow wow"]


pre = 0
req = 0
poke=on_notice()
@poke.handle()
async def _(matcher: Matcher,event:Event):
    try:
        if isinstance(event,PokeNotifyEvent):
            if event.is_tome() and event.user_id !=event.self_id:
                l = len(a)
                k = random.randint(0,l-1)
                while pre == k:
                    k = random.randint(0,l-1)
                await matcher.send(a[k],at_sender=True)
    except Exception as e:
        await poke.send("戳一戳插件出现故障，请联系阿弟")

chehui = on_notice()
@chehui.handle()
async def cheh(matcher: Matcher,event:GroupRecallNoticeEvent):
    try:
        if event.user_id == event.operator_id :
            if event.operator_id!= event.self_id:
                l=len(xiuxiu)
                k = random.randint(0,l-1)
                while req == k:
                    k = random.randint(0,l-1)
                await matcher.send(
                    message=xiuxiu[k],
                    at_sender=True
                  )
    except Exception as e:
        await chehui.send("撤回插件出现故障，请联系阿弟")

regbag = on_notice()
@regbag.handle()
async def redb(matcher: Matcher,event:LuckyKingNotifyEvent):
    try:
        atmsg = MessageSegment.at(event.target_id)
        await matcher.send(
            event=event,
            message = atmsg+'恭喜你是运气王，请立即红包接力，不要不识好歹',
        )
    except Exception as e:
        await regbag.send("运气王插件出现故障，请联系阿弟")

sao=on_command(cmd="骚话",aliases={"马叉虫"},priority=3)
@sao.handle()
async def print_sao(matcher: Matcher):
    url="https://api.iyk0.com/sao"
    httpText=httpx.get(url)
    await matcher.finish(MessageSegment.text(httpText))
    
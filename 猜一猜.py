from nonebot.adapters.onebot.v11 import MessageSegment,Message,Event
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.matcher import Matcher
from nonebot import on_command
import httpx
import json
import asyncio
import random
import requests
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name='猜一猜',
    description='益智小游戏',
    usage='发送 猜一猜(猜成语,猜字谜)',
    extra={
        'author': 'hamo-reid',
        'menu_template': 'default'
    }
)

cd=30

encourage_list=["不对哦，再猜猜","不对哦，再努力想一下吧","加油！你可以的"]

idiomList=dict()

idiom=on_command(cmd="猜一猜",aliases={"猜成语"},priority=3)

@idiom.handle()
async def  my_Func(matcher: Matcher,event: Event,args: Message = CommandArg()):
    user_id=event.get_user_id()
    url="http://api.tianapi.com/riddle/index?key=113685e9774db2c898fdb3e123538348"
    http=httpx.get(url)
    res=json.loads(http.text)
    newslist=res["newslist"]
    key=newslist["key"][0]["answer"]
    idiomList[user_id]=key
    await matcher.send(Message(newslist["newslist"][0]["quest"]) + Message("30秒后公布答案"))
    loop = asyncio.get_running_loop()
    loop.call_later(cd,lambda:asyncio.ensure_future(get_key(matcher,key,user_id)))


@idiom.got("idion",prompt="来猜一猜吧")
async def _(matcher: Matcher,event: Event,idion_key: str = ArgPlainText("idion")):
    user_id=event.get_user_id()
    if idion_key==idiomList[user_id]:
        del idiomList[user_id]
        await matcher.send("恭喜你答对了")
        await matcher.finish(Message("奖励你一张图片") + MessageSegment.image("https://www.dmoe.cc/random.php"),at_sender=True)
    else: await matcher.reject(random.choice(encourage_list))


async def get_key(matcher:Matcher,key,user_id):
    if user_id in idiomList:
        del idiomList[user_id]
        await matcher.finish("失败了捏,答案是"+key)


Riddle=on_command("猜字谜",aliases={"字谜"},priority=3)



@Riddle.handle()
async def Fanc_1(matcher: Matcher,event: Event,args: Message = CommandArg()):
   user_id=event.get_user_id()
   url="http://api.tianapi.com/zimi/index"
   deta={"key":"113685e9774db2c898fdb3e123538348"}
   res=requests.get(url,deta)
   res=json.loads(res.text)
   content=res["newslist"][0]["content"]
   answer=res["newslist"][0]["answer"]
   tis=res["newslist"][0]["reason"]
   await matcher.send(content,at_sender=True)
   await Riddle.send("30秒后公布答案")
   idiomList[user_id]=[answer,tis]
   loop = asyncio.get_running_loop()
   loop.call_later(cd,lambda:asyncio.ensure_future(get_Riddle(matcher,answer,tis,user_id)))

@Riddle.got("riddle","快来开动你的小脑筋")
async def MyRiddle(matcher: Matcher,event: Event,idion_key: str = ArgPlainText("riddle")):
    user_id=event.get_user_id()
    if idion_key==idiomList[user_id]:
        del idiomList[user_id]
        await matcher.send("恭喜你答对了")
        await matcher.finish(Message("奖励你一张美图") + MessageSegment.image("https://www.dmoe.cc/random.php"),at_sender=True)
    else: await matcher.reject(encourage_list[int(random.randrange(0,len(encourage_list)))])

async def get_Riddle(matcher:Matcher,answer,tis,user_id):
    if user_id in idiomList:
        del idiomList[user_id]
        await matcher.finish("失败了捏,答案是"+answer+","+"提示："+tis)

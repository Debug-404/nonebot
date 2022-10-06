from nonebot.adapters.onebot.v11 import MessageSegment,Message,Event
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.matcher import Matcher
from nonebot import on_command
import requests
import json

continuity=on_command(cmd="成语接龙",priority=3)
my_list=['113685e9774db2c898fdb3e123538348','2c15555dcbbded34aa9ed6f2a45ad9a0']
Num=0
#idiomList=dict()

@continuity.handle()
async def get_continuity(matcher:Matcher,event: Event,args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("idiom", args)

@continuity.got("idiom","你先说吧")
async def get_continuity_got(matcher: Matcher,event: Event,continuity_key: str = ArgPlainText("idiom")):
    user_id=event.get_user_id()
    text=await get_key(continuity_key,user_id)
    if text["code"]==200:
        if text["newslist"][0]["result"] in [2,3,4]:
            await matcher.finish("回答错误！游戏结束")
        elif text["newslist"][0]["result"] in [0,1]:
            await matcher.reject(text["newslist"][0]["tip"])
        else:await matcher.finish("关系你赢了")
    else:
        if Num==0:
            Num=1
        else:Num=0
        await matcher.finish("出现故障或者可使用次数不够，请联系阿弟")
    

async def get_key(key:str,user_id:str):
    url="http://api.tianapi.com/chengyujielong/index"
    data={"key":my_list[Num],
        "userid":user_id,
        "word":key,
        "statetime":1800}
    res=requests.post(url,data)
    res=json.loads(res.text)
    return res
from nonebot.adapters.onebot.v11 import Message,Event,GROUP
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.matcher import Matcher
from nonebot import on_command,on_message
from nonebot.rule import to_me
import requests
import json

digua=on_message(rule=to_me(),priority=2,permission=GROUP)

@digua.handle()
async def Sweet_potato(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("idnex", args)

@digua.got("idnex",prompt="小女子在，有什么事要吩咐吗")
async def got_Sweet_potato(matcher: Matcher,idnex: Message = Arg(), instructions: str = ArgPlainText("idnex")):
    if instructions not in ["下去吧","可以了","拜拜"]:
        digua_text = await get_instructions(instructions)
        await matcher.reject(digua_text)
    else:await matcher.finish("小女子告退了")


async def get_instructions(instructions:str):
    url = f'http://api.qingyunke.com/api.php?key=free&appid=0&msg={instructions}'
    res=requests.get(url)
    url_text=json.loads(res.text)
    answer=url_text["content"]
    print("hello")
    if "{br}" in answer:
        answer=answer.replace("{br}","\n")
    if "菲菲" in answer:
        answer=answer.replace('菲菲','地瓜')
    if "{face:" in answer:
        num1=answer.find("{")
        numn2=answer.find("}")
        face_id=answer[answer.find("{")+6:answer.find("}")]
        CQ=f"[CQ:face,id={face_id}]"
        return Message(CQ)+Message(str(answer[numn2+1:]))+Message("(Tips:拜拜可以退出对话)")
    else:
        return Message(f'{answer}')+Message("(Tips:拜拜可以退出对话)")

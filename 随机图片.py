from nonebot.adapters.onebot.v11 import Message,Event,MessageSegment
from nonebot.matcher import Matcher
from nonebot import on_command
import requests 
import random
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name='每日一图',
    description='随机发送一张图片',
    usage='发送指令[每日一图,随机图片,每日亿图,亿张图片]',
    extra={
        'author': 'hamo-reid',
        'menu_template': 'default'
    }
)

get_img=on_command("每日一图",aliases={"随机图片","每日亿图","亿张图片"},priority=2)
@get_img.handle()
async def return_img(matcher:Matcher,event:Event):
    url=["https://iw233.cn/api/Random.php","https://api.ixiaowai.cn/api/api.php"]
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
    res = requests.get(random.choice(url),headers=headers)
    await matcher.finish(message=MessageSegment.image(res.url),at_sender=True)


    
    
    
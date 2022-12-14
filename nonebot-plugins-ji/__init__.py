import random
from nonebot.plugin.on import on_command
from nonebot.adapters.onebot.v11 import Bot,  GroupMessageEvent
from nonebot.adapters.onebot.v11.helpers import Cooldown
from nonebot.adapters.onebot.v11.message import MessageSegment
import os
from pathlib import Path
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name='寄',
    description='寄',
    usage='寄(ji)',
    extra={
        'author': 'hamo-reid',
        'menu_template': 'default'
    }
)

random.seed(1)

jitu = [
    "1.jpg",
    "2.jpg",
    "3.jpg",
    "4.jpg",
    "5.jpg",
    "6.jpg",
    "7.jpg",
    "8.jpg",
    "9.jpg",
    "10.jpg",
    "11.jpg",
    "12.jpg",
    "13.jpg",
    "14.jpg",
    "15.jpg",
    "16.jpg",
    "17.jpg",
    "18.jpg",
    "19.jpg",
    "20.jpg",
    "21.jpg",
    "22.jpg",
    "23.jpg",
    "24.jpg",
    "25.jpg",
    "26.jpg",
    "27.jpg",
    "28.jpg",
    "29.jpg",
    "30.jpg",
    "31.jpg",
    "32.jpg",
    "33.jpg",
    "34.jpg",
    "35.jpg",
    "36.jpg",
    "37.jpg",
    "38.jpg",
    "39.jpg",
    "40.jpg",
    "41.jpg",
    "42.jpg",
    "43.jpg",
    "44.jpg",
    "45.jpg",
    "46.jpg",
    "47.jpg",
    "48.jpg",
    "49.jpg",
    "50.jpg",
    "51.jpg",
    "52.jpg",
    "53.jpg",
    "54.jpg",
    "55.jpg",
    "56.jpg",
    "57.jpg",
    "58.jpg",
    "59.jpg",
    "60.jpg",
    "61.jpg",
    "62.jpg",
    "63.jpg",
    "64.jpg",
    "65.jpg",
    "66.jpg",
    "67.jpg",
    "68.jpg",
    "69.jpg",
    "70.jpg",
    "71.jpg",
    "72.jpg",
    "73.jpg",
    "74.jpg",
    "75.jpg",
    "76.jpg",
    "1.gif",
    "2.gif",
    "3.gif",
    "4.gif",
    "5.gif",
    "6.gif",
    "7.gif",
    "8.gif",
    "9.gif",
    "10.gif",
    "11.gif",
    "12.gif",
]

jile = on_command("寄", aliases={"ji"}, priority=20, block=True)



@jile.handle()
async def _jile(bot: Bot, event: GroupMessageEvent):
    tu=f"{random.choice(jitu)}"
    await jile.finish(MessageSegment.image(Path(os.path.join(os.path.dirname(__file__), "resource"))/ tu))
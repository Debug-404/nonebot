from nonebot.matcher import Matcher
from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import (
    GroupMessageEvent,
    Message,
    MessageSegment,
    Bot,
    MessageEvent,
    PrivateMessageEvent,
)
from nonebot.exception import ActionFailed
from nonebot.plugin import PluginMetadata
from nonebot.log import logger
import wenxin_api
from wenxin_api.tasks.text_to_image import TextToImage

__plugin_meta__ = PluginMetadata(
    name="百度文心api",
    description="以文本生成图片",
    usage="""
    usage：
    用图片描述+图片风格生成图片
    指令：
        以文生图 图片风格  图片描述
    图片描述请不要带空格！      
    风格可以是：油画、水彩、二次元、粉笔画、儿童画、蜡笔画、 卡通、古风、像素风格、蒸汽波艺术、赛博朋克、概念艺术、未来主义、写实风格、超现实主义
    """,
    extra={"author": "hamo-reid", "menu_template": "default"},
)

wenxin_api.ak = "Uzbwu7EYZHiVoofbfuIpvnS6u1jP98NG"
wenxin_api.sk = "tXAkdEv2iUfSH1uRHoc2WbrbAaK6BrGQ"

styleList = [
    "古风",
    "油画",
    "二次元",
    "粉笔画",
    "儿童画",
    "蜡笔画",
    "卡通",
    "像素风格",
    "蒸汽波艺术",
    "赛博朋克",
    "概念艺术",
    "未来主义",
    "写实风格",
    "超现实主义",
    "洛丽塔风格",
    "",
]


tips = "请输入正确的格式：以文生图 图片风格 图片描述\n风格可以是：二次元、水彩、卡通、粉笔画、儿童画、蜡笔画"

pic = on_command("以文生图", aliases={"生成图片"}, priority=5, block=True)


@pic.handle()
async def printImg(
    bot: Bot,
    event: MessageEvent,
    msg: Message = CommandArg(),
):
    msg = msg.extract_plain_text().strip().split()
    logger.info(msg)
    style = msg[0]
    if len(msg) < 2:
        await pic.finish(tips)
    elif style not in styleList:
        await pic.finish(tips)
    else:
        tag = ",".join(msg[1:])
        await pic.send("请稍等，图片生成中。。。")
        imgList = await getImg(pic, tag, style)
        try:
            if isinstance(event, PrivateMessageEvent):
                for msg in imgList:
                    await pic.send(MessageSegment.image(msg))
            elif isinstance(event, GroupMessageEvent):
                msgs = [
                    to_json(MessageSegment.image(msg), "地瓜", bot.self_id)
                    for msg in imgList
                ]
                await bot.call_api(
                    "send_group_forward_msg", group_id=event.group_id, messages=msgs
                )
        except ActionFailed as e:
            await pic.finish(message=Message(f"消息被风控了捏，图发不出来"), at_sender=True)


async def getImg(
    pic: Matcher, tag: str, style: str = "二次元", Resolution: str = "1536*1024"
) -> list[str]:
    input_dict = {"text": f"{tag}，细节清晰，高清，8k", "style": style, "resolution": Resolution}
    rst = TextToImage.create(**input_dict)
    if "imgUrls" in rst:
        return rst["imgUrls"]
    else:
        await pic.finish(tips)


def to_json(msg, name: str, uin: str):
    return {"type": "node", "data": {"name": name, "uin": uin, "content": msg}}

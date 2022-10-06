from nonebot.plugin import on_notice
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent,GroupDecreaseNoticeEvent

welcom=on_notice()

@welcom.handle()
async def welcome(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
    user = event.get_user_id()
    at_ = "欢迎！：[CQ:at,qq={}]".format(user)
    msg = at_ + '大佬加入聊天组'
    msg = Message(msg)
    await welcom.finish(message=Message(f'{msg}'))

@welcom.handle()
async def welcome(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):
    user = event.get_user_id()
    msg = "{}退出了聊天组".format(user)
    msg = Message(msg)
    await welcom.finish(message=Message(f'{msg}'))


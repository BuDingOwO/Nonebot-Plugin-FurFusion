import json

from nonebot import get_driver
from .config import Config
from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageEvent, Event, Bot, GroupMessageEvent
from nonebot.params import CommandArg, ArgPlainText, Arg
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
import json
from .Network import *

global_config = get_driver().config
config = Config.parse_obj(global_config)

cmd = on_command(cmd="查兽聚信息", aliases={"FurryFusion"}, priority=config.priority, block=True)


@cmd.handle()
async def __(bot: Bot, event: Event, args: Message = CommandArg()):
    MAX_DISPLAY_CLU = 2
    MAX_DISPLAY_ROW = 10
    msg = str(event.get_message())
    CmdArgs = args.extract_plain_text().split(" ")
    if CmdArgs[0] == "":
        res = await getInfo("", "")
        data = res["data"]
        Len = len(data)
        if Len > 10:
            l1 = data[0, 10]
            l2 = data[11, Len]
        


    elif CmdArgs[0] == "城市":
        res = await getInfo("city", CmdArgs[1])
    elif CmdArgs[0] == "票务状态":
        # 0.无状态 1.预告中 2.售票中 3.报名中
        # 4.延期中 5.已售空 6.预热中
        Ticket = CmdArgs[1].replace("无状态", "0").replace("预告中", "1").replace("售票中", "2").replace("报名中", "3")
        Ticket = Ticket.replace("延期中", "4").replace("已售空", "5").replace("预热中", "6")
        res = await getInfo("ticket", Ticket)
    elif CmdArgs[0] == "兽聚状态":
        # 0.正常举办 1.举办待定 2.停止运营
        # 3. 数据校验 4.状态未知 5.连接丢失
        State = CmdArgs[1].replace("正常举办", "0").replace("举办待定", "1").replace("停止运营", "2").replace("数据校验", "3")
        State = State.replace("状态未知", "4").replace("连接丢失", "5")
        res = await getInfo("state", State)
    elif CmdArgs[0] == "新的":
        res = await getInfo("new", "")





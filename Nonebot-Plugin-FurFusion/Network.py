import aiohttp

BaseURL = " https://www.furrystudio.net/api/furryfusion"


async def getInfo(rule: str, data: str):
    """
    兽聚信息
    :param rule: str Null|city|ticket|state|new
    :param data: str
    :return:
    """
    APIPath = "/inquire/list?rule={rule}&data={data}".format(rule=rule, data=data)
    """
    if rule == "":  # 返回完整的兽聚信息列表 data留空
        APIPath.format(rule="", data="")
    elif rule == "city":  # data输入预查找到城市名称
        APIPath.format(rule=rule, data="")
    elif rule == "ticket":  # 预查找的票务状态(数字标号) 0.无状态 1.预告中 2.售票中 3.报名中 4.延期中 5.已售空 6.预热中
        APIPath.format(rule="", data="")
    elif rule == "state":  # 预查找的兽聚状态(数字标号) 0.正常举办 1.举办待定 2.停止运营 3. 数据校验 4.状态未知 5.连接丢失
        APIPath.format(rule="", data="")
    elif rule == "new":  # 查找所有新兽聚（本项留空）
        APIPath.format(rule="", data="")"""

    async with aiohttp.ClientSession() as session:
        async with session.get(BaseURL + APIPath) as res:
            return res


async def getMoreInfo(tab: str):
    """
    Get 兽聚详情信息
    :param tab: str 对应兽聚标号
    :return:
    """
    APIPath = "/inquire/details?tab={tab}".format(tab=tab)
    async with aiohttp.ClientSession() as session:
        async with session.get(BaseURL + APIPath) as res:
            return res


async def getTimeLine(tab: str):
    """
    Get 兽聚时间线信息
    :param tab: str 对应兽聚标号
    :return:
    """
    APIPath = "/inquire/timeline?tab={tab}".format(tab=tab)
    async with aiohttp.ClientSession() as session:
        async with session.get(BaseURL + APIPath) as res:
            return res

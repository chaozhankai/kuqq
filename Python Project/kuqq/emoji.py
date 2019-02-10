# 把/斜眼笑这些变成cq码，复读成对应表情
emoji_list = {
    "/泪奔": "[CQ:face,id=173]",
    "/无奈": "[CQ:face,id=174]",
    "/卖萌": "[CQ:face,id=175]",
    "/小纠结": "[CQ:face,id=176]",
    "/喷血": "[CQ:face,id=177]",
    "/斜9眼7笑": "[CQ:face,id=178]",
    "/斜眼笑": "[CQ:face,id=178]",
    "/doge": "[CQ:face,id=179]",
    "/惊喜": "[CQ:face,id=180]",
    "/骚扰": "[CQ:face,id=181]",
    "/笑哭": "[CQ:face,id=182]",
    "/我最美": "[CQ:face,id=183]",
    "/幽灵": "[CQ:face,id=187]"}


def emoji2cq(message: str):
    for emoji in emoji_list:
        message = message.replace(emoji, emoji_list[emoji])
    return message

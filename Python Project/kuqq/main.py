from aiocqhttp import CQHttp
import emoji
# pip3 install aiocqhttp
# 说明文档 https://github.com/richardchien/python-aiocqhttp/blob/master/README.md

bot = CQHttp(enable_http_post=False)


@bot.on_message()
async def handle_msg(context):
    # 判断群号，不复读个别破群
    group_id = context.get('group_id')
    # 判断QQ号，不复读个别幺儿
    sender_qq = context.get('user_id')
    if group_id in [617166836]:
        return ""
    if group_id in [140399496]:
        return ""
    # 不复读狗栀
    if sender_qq in [1400525500]:
        return ""
    message = context['message']
    # 增加对/斜眼笑等表情的处理
    await bot.send(context, emoji.emoji2cq(message).replace('吗', "").replace('?', '!').replace('？', '!'))
    # await bot.send(context, context['message'].replace('吗', "").replace('?', '!').replace('？', '!'))

bot.run(host='127.0.0.1', port=9898)
# 今儿居然就加上了复读表情！

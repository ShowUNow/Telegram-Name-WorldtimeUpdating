#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Updated:
#  1. 使用async来update lastname，更加稳定
#  2. 增加emoji clock，让时间显示更加有趣味

import pytz
import time
import os
import sys
import logging
import asyncio
import random
from datetime import datetime, timedelta
from time import strftime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from emoji import emojize


all_time_emoji_name = ["clock12", "clock1230", "clock1", "clock130", "clock2", "clock230", "clock3", "clock330", "clock4", "clock430", "clock5", "clock530", "clock6", "clock630", "clock7", "clock730", "clock8", "clock830", "clock9", "clock930", "clock10", "clock1030", "clock11", "clock1130"]
time_emoji_symb = [emojize(":%s:" % s, use_aliases=True) for s in all_time_emoji_name]

# 添加旗帜类表情
soybean_emojis = [emojize(":smile:", use_aliases=True), emojize(":laughing:", use_aliases=True), emojize(":blush:", use_aliases=True), emojize(":smiley:", use_aliases=True), emojize(":relaxed:", use_aliases=True)]

api_auth_file = 'api_auth'
if not os.path.exists(api_auth_file+'.session'):
    api_id = input('api_id: ')
    api_hash = input('api_hash: ')
else:
    api_id = 123456
    api_hash = '00000000000000000000000000000000'

client1 = TelegramClient(api_auth_file, api_id, api_hash)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# 获取datetime 的函数
def get_naive_datetime(dt):
    return dt.replace(tzinfo=None)

async def change_name_auto():
    print('will change name')

# 定义时区和夏令时
    timezones = {
    '亚洲/东京': ('Asia/Tokyo', 'UTC+9'),
    '欧洲/莫斯科': ('Europe/Moscow', 'UTC+3'),
    '亚洲/上海': ('Asia/Shanghai', 'UTC+8'),
    '美国/东部': ('US/Eastern', 'UTC-5'),
    '美国/太平洋': ('US/Pacific', 'UTC-8'),
    '格林尼治标准时间': ('Etc/GMT', 'UTC+0'),
    '澳大利亚/悉尼': ('Australia/Sydney', 'UTC+10'),
    '非洲/约翰内斯堡': ('Africa/Johannesburg', 'UTC+2'),
    '亚洲/加尔各答': ('Asia/Kolkata', 'UTC+5:30'),
    '欧洲/柏林': ('Europe/Berlin', 'UTC+1'),
    '欧洲/伦敦': ('Europe/London', 'UTC+0'),
    '亚洲/迪拜': ('Asia/Dubai', 'UTC+4'),
    '美国/纽约': ('America/New_York', 'UTC-5'),
    '美国/洛杉矶': ('America/Los_Angeles', 'UTC-8'),
    '美国/芝加哥': ('America/Chicago', 'UTC-6'),
    '亚洲/新加坡': ('Asia/Singapore', 'UTC+8'),
    '亚洲/香港': ('Asia/Hong_Kong', 'UTC+8'),
    '亚洲/首尔': ('Asia/Seoul', 'UTC+9'),
    '非洲/内罗毕': ('Africa/Nairobi', 'UTC+3'),
    '非洲/开罗': ('Africa/Cairo', 'UTC+2'),
    '非洲/拉各斯': ('Africa/Lagos', 'UTC+1'),
    '亚洲/马尼拉': ('Asia/Manila', 'UTC+8'),
    '亚洲/台北': ('Asia/Taipei', 'UTC+8'),
    '美洲/圣地亚哥': ('America/Santiago', 'UTC-4'),
    '欧洲/巴黎': ('Europe/Paris', 'UTC+1')
}
    flag_emojis = {
    '亚洲/东京': '🇯🇵',
    '欧洲/莫斯科': '🇷🇺',
    '亚洲/上海': '🇨🇳',
    '美国/东部': '🇺🇸',
    '美国/太平洋': '🇺🇸',
    '格林尼治标准时间': '🌍',
    '澳大利亚/悉尼': '🇦🇺',
    '非洲/约翰内斯堡': '🇿🇦',
    '亚洲/加尔各答': '🇮🇳',
    '欧洲/柏林': '🇩🇪',
    '欧洲/伦敦': '🇬🇧',
    '亚洲/迪拜': '🇦🇪',
    '美国/纽约': '🇺🇸',
    '美国/洛杉矶': '🇺🇸',
    '美国/芝加哥': '🇺🇸',
    '亚洲/新加坡': '🇸🇬',
    '亚洲/香港': '🇭🇰',
    '亚洲/首尔': '🇰🇷',
    '非洲/内罗毕': '🇰🇪',
    '非洲/开罗': '🇪🇬',
    '非洲/拉各斯': '🇳🇬',
    '亚洲/马尼拉': '🇵🇭',
    '亚洲/台北': '🇹🇼',
    '美洲/圣地亚哥': '🇨🇱',
    '欧洲/巴黎': '🇫🇷'
}

    
    while True:
        try:
            time_cur = datetime.now(pytz.timezone('Asia/Taipei')).strftime("%H:%M:%S:%p:%a")
            hour, minu, seco, p, abbwn = time_cur.split(':')
            if seco == '00':
                shift = 0
                mult = 1
                if int(minu) > 30:
                    shift = 1
                
                for_fun = random.random()

                for tz_name, (tz, utc_offset) in timezones.items():
                    if for_fun < 0.04:
                        target_tz = pytz.timezone(tz)
                        target_time = datetime.now(target_tz)
                        target_time = get_naive_datetime(target_time)  
                        if target_tz.dst(target_time) != timedelta(0):
                            target_time += target_tz.dst(target_time)
                            
                        flag_emoji = flag_emojis.get(tz_name, '🏳️')
                        first_name = f'{tz_name} {flag_emoji}'
                        time_cur = target_time.strftime("%H:%M:%S:%p:%a")
                        hour, minu, seco, p, abbwn = time_cur.split(':')
                        # 小时符号
                        hsym = time_emoji_symb[(int(hour) % 12) * 2 + shift]
                        last_name = f'{target_time.strftime("%H:%M %p")} {utc_offset} {hsym}'
                        break
                    for_fun -= 0.04

                await client1(UpdateProfileRequest(last_name=last_name))
                await client1(UpdateProfileRequest(first_name=first_name))
                logger.info('Updated -> %s' % last_name)
        
        except KeyboardInterrupt:
            print('\nwill reset last name\n')
            await client1(UpdateProfileRequest(last_name=''))
            sys.exit()

        except Exception as e:
            print('%s: %s' % (type(e), e))

        await asyncio.sleep(1)


# main function
async def main(loop):

    await client1.start()

    # create new task
    print('creating task')
    task = loop.create_task(change_name_auto())
    await task
     
    print('It works.')
    await client1.run_until_disconnected()
    task.cancel()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))

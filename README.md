# Telegram-Name-WorldtimeUpdating  

The name of the telegram can be changed every minute to the time in different parts of the world

参考文档：<a href="https://telethon.readthedocs.io/en/stable/">Telethon</a>

Name实时更新效果：<a href="https://t.me/mainjor">(https://t.me/mainjor)</a>

<code>
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
</code>

## 0. 准备

运行环境：VPS，python3，python3-pip

创建应用：<a href="https://my.telegram.org/">https://my.telegram.org/</a>。只要填App title和Short name即可。获得api_id和api_hash。

## 1. 下载Demo小程序到VPS上

<code>git clone https://github.com/showunow/Telegram-Name-WorldtimeUpdating.git</code>\
<code>cd Telegram-Name-Updating</code>

## 2. 安装telethon

<code>pip3 install -r requirements.txt</code>

## 3. 运行

<code>python3 tg_name.py</code>

## 4. api认证和用户登陆

根据提示输入api_id和api_hash。接着输入手机号和验证码，如果账号开启了二次验，证根据提示再输入二次验证的密码。最后看到 It works! 表明成功了。


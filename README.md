# get-tg-msg-reactions
获取telegram群消息表情点赞的记录

<img width="705" height="200" alt="image" src="https://github.com/user-attachments/assets/1cb3946a-f920-4e8e-b253-4b4037a062f6" />

api_id, api_hash 需要自己申请  
my.telegram.org  
具体步骤不写了, 自己去问 google 和 gpt  

url 就填 右键 - 复制消息链接 的结果  
<img width="498" height="500" alt="image" src="https://github.com/user-attachments/assets/425d9521-0434-4f72-92d8-ef46c4931443" />

## 搭环境
```
apt install -y python3-pip
pip3 install telethon --break-system-packages
```

## 运行
```
python3 tg-get-msg-reactions.py
```

## 运行结果示例
```
获取所有反应的用户：
1. User: 372552030, Name: ㅤ, Reaction: 👏, Time: 2025-09-13 04:49:14
2. User: dshowme, Name: dshow, Reaction: 👍, Time: 2025-09-13 03:07:23
3. User: pnpat, Name: Pat, Reaction: 👍, Time: 2025-09-13 03:01:58
4. User: 5760032256, Name: Macario, Reaction: 👍, Time: 2025-09-13 02:51:57
5. User: 8038895285, Name: Ghbn Vds, Reaction: 👍, Time: 2025-09-13 02:48:52
6. User: comfortable198, Name: @xxiedj_bot, Reaction: 👍, Time: 2025-09-13 02:22:07
7. User: ze0621mwz2198, Name: 鉴黄师 🔞人体结构 研究小组, Reaction: 👍, Time: 2025-09-12 23:48:35
```

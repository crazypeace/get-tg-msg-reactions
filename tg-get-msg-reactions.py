import asyncio
import re
from telethon import TelegramClient
from telethon.tl.functions.messages import GetMessageReactionsListRequest
from telethon.utils import get_display_name
from telethon.errors import ChannelInvalidError, ChannelPrivateError

def parse_tg_url(url: str):
    """
    从 t.me/c/1517821953/51108 解析出 chat_id, msg_id
    从 t.me/username/12345 解析出 username, msg_id
    """
    m1 = re.match(r'https://t\.me/c/(\d+)/(\d+)', url)
    if m1:
        chat_id = int('-100' + m1.group(1))
        msg_id = int(m1.group(2))
        return chat_id, msg_id

    m2 = re.match(r'https://t\.me/([\w\d_]+)/(\d+)', url)
    if m2:
        username = m2.group(1)
        msg_id = int(m2.group(2))
        return username, msg_id
    
async def get_all_reactions(chat_id: int, msg_id: int, api_id: str, api_hash: str) -> list:
    """
    获取消息的所有反应（不指定特定emoji）
    """
    async with TelegramClient('session2', api_id, api_hash) as client:
        try:
            entity = await client.get_entity(chat_id)
            peer = await client.get_input_entity(entity)
            
            # 不指定 reaction 参数来获取所有反应
            result = await client(GetMessageReactionsListRequest(
                peer=peer,
                id=msg_id,
                limit=100
            ))
            
            users_reactions = []
            for reaction in result.reactions:
                try:
                    user = await client.get_entity(reaction.peer_id)
                    reaction_time = reaction.date.strftime('%Y-%m-%d %H:%M:%S')
                    reaction_emoji_str = reaction.reaction.emoticon if hasattr(reaction.reaction, 'emoticon') else 'Unknown'
                    display_name = get_display_name(user)
                    users_reactions.append((
                        user.username if getattr(user, 'username', None) else user.id,
                        display_name,
                        reaction_emoji_str,
                        reaction_time
                    ))
                except Exception as e:
                    print(f"Failed to get user for peer_id {reaction.peer_id}: {e}")
                    continue
            return users_reactions
            
        except ChannelInvalidError:
            print(f"Invalid channel ID: {chat_id}. Ensure the client is a member of the channel.")
            return []
        except ChannelPrivateError:
            print(f"Channel {chat_id} is private. Ensure the client has access.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

async def main():    
    api_id = '12345678'    
    api_hash = 'f9847f9847f9847f9847f9847f984747'
    url = 'https://t.me/c/1517821953/51108'
    # url = 'https://t.me/tg233boy/1206848'
    chat_id, msg_id = parse_tg_url(url)

    # 获取所有反应
    print("获取所有反应的用户：")
    all_reactions = await get_all_reactions(chat_id, msg_id, api_id, api_hash)
    if all_reactions:
        for idx, (user, display_name, reaction_emoji, timestamp) in enumerate(all_reactions, 1):
            print(f"{idx}. User: {user}, Name: {display_name}, Reaction: {reaction_emoji}, Time: {timestamp}")
    else:
        print("No reactions found or an error occurred.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

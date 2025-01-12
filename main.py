import requests
import os

def get_guild_emojis(server_id, user_token):
    url = f"https://discord.com/api/v10/guilds/{server_id}"
    headers = {
        "Authorization": user_token,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        guild_data = response.json()
        emojis = guild_data.get("emojis", [])

        if not os.path.exists('emojis'):
            os.makedirs('emojis')

        for emoji in emojis:
            emoji_id = emoji['id']
            emoji_name = emoji['name']
            animated = emoji['animated']
            extension = 'gif' if animated else 'png'
            emoji_url = f"https://cdn.discordapp.com/emojis/{emoji_id}.{extension}"

            emoji_response = requests.get(emoji_url)

            if emoji_response.status_code == 200:
                with open(f'emojis/{emoji_name}.{extension}', 'wb') as f:
                    f.write(emoji_response.content)
                print(f"Downloaded: {emoji_name}")
            else:
                print(f"Failed to download: {emoji_name}")
    else:
        print(f"Failed to fetch guild data. Status code: {response.status_code}")

server_id = "SERVER ID"
user_token = "YOUR TOKEN DONT SHARE IT WITH NO ONE"
get_guild_emojis(server_id, user_token)

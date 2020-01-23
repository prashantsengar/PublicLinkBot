# tgfilestream - A Telegram bot that can stream Telegram files to users over HTTP.
# Copyright (C) 2019 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.'
import logging

from telethon import TelegramClient, events

from .paralleltransfer import ParallelTransferrer
from .config import session_name, api_id, api_hash, public_url
from .util import pack_id, get_file_name

log = logging.getLogger(__name__)

client = TelegramClient(session_name, api_id, api_hash)
transfer = ParallelTransferrer(client)


@client.on(events.NewMessage)
async def handle_message(evt: events.NewMessage.Event) -> None:
    if not evt.is_private or not evt.file:
        return

    filename = get_file_name(evt)
    url = str(public_url)+ '/'+ str(pack_id(evt)) + '/' +str(filename)
    print(url)

    watch_url = str(public_url)+'/watch/'+str(pack_id(evt))+'/' + filename
    await evt.reply(f"Link to download file: [{watch_url}]({watch_url})")
    log.info(f"Replied with link for {evt.id} to {evt.from_id} in {evt.chat_id}")
    log.info(f"Link to {evt.id} in {evt.chat_id}: {watch_url}...{url}")

def add_user(idd):
    file = open('user.txt')
    file.write(idd)
    file.write('\n')
    file.close()

@client.on(events.NewMessage(pattern='/start', forwards=False))
async def handler(event):
    message = await event.reply('Hi! The @PublicDownloadLinkBot can give you a direct streaming and download link of any file present on Telegram (without any ads).\nSend any file from Telegram, I will send you a direct link to stream it on your browser! You will also be able to download the file!\n\n**How to use?**\n- Forward a file to me\n- I will reply with a streaming link of the file\n- To download the file, open that link and click on the Download button\n *Note* : Your Chrome browser may not support streaming of video files. In case of problems, try another browser like Firefox or Edge. \nSee /help for more')

    try:
        add_user(event.chat_id)
    except Exception as e:
        log.warning(e)

@client.on(events.NewMessage(pattern='/help', forwards=False))
async def handler(event):
    message = await event.reply('Hi! This is the @PublicDownloadLinkBot. I can give you a direct streaming and download link of any file present on Telegram (without any ads).\n**How is it better than other bots?** \n-It is superfast and gives you a direct link instantly unlike other bots that take up too much time\n-The file link is directly of Telegram\'s servers so the download and streaming speed is very fast.\n- No ads on the website! \n\nSend any file from Telegram, I will send you a direct link to stream it on your browser! **You will also be able to download the file!**\n\n**How to use?**\n- Forward a file to me\n- I will reply with a streaming link of the file\n- To download the file, open that link and click on the Download button\n \n*Note* : Your Chrome browser may not support streaming of video files. In case of problems, try another browser like Firefox or Edge. \n\n\nJoin @PublicLinkBotUpdates to discuss about this bot')

  

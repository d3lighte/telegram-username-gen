from pyrogram.errors import UsernameInvalid, UsernameNotOccupied
from config import app_id, hash_id
from pyrogram import Client
from loguru import logger
import aiofiles

async def checkName(account):
   async with Client('account', app_id, hash_id) as app:              
        try:
            await app.get_users(account)
            logger.error(f'@{account} - > username is unavailable')
        except UsernameNotOccupied:
            logger.info(f'@{account} - > username is awaible')
            async with aiofiles.open('data/usernames.txt', 'r+') as file:
                await file.read()
                await file.write(account + '\n')
        except UsernameInvalid:
                 logger.error(f'{account} - > username is invalid')
        except IndexError:
              logger.error(f'{account} -> username is unavailable')
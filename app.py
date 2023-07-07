from scripts.names import getRandomName
from scripts.check import checkName
from asyncio import run
from loguru import logger

async def start():
    cycles = input('Number of loops\nor write "N" for while True cycle\nEnter type: ')
    alphabet = input('enter alphabet or "n" to use default -> ')
    if alphabet.lower() in ('n', 'no'):
        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    lenght = int(input('enter len to username -> '))
    if lenght >= 5:
        if cycles.lower() in ("n", "no"):
            while True: 
                username = getRandomName(alphabet, lenght)
                await checkName(username)
        else:
            for _ in range(int(cycles)):
                username = getRandomName(alphabet, lenght)
                await checkName(username)                
    else: 
        logger.error('In lenght must 4+ simbols.')

run(start())
"""
    Test Module
    Licensed under the Apache License, Version 2.0
    Authors: Your Name
"""
import logging
from telethon import events
from telethon.tl.patched import Message
from typing import List, Union
from modules.loader import Module
from modules import utils

# Настройка логирования для модуля
logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
logger.setLevel(logging.DEBUG)  # Установите на DEBUG для подробных логов

class TestModule(Module):
    """
    Test Module for verifying dynamic loading
    """
    strings = {
        'name': 'TestModule',
        'testcmd_response': 'Тестовая команда работает!'
    }

    def __init__(self, client):
        super().__init__(client)
        self.register_handlers()
        logger.info("TestModule инициализирован и обработчики зарегистрированы.")

    def register_handlers(self):
        self.client.add_event_handler(self.testcmd, events.NewMessage(pattern=r"\.testcmd"))
        logger.info("Обработчик команды .testcmd зарегистрирован.")

    async def testcmd(self, event: Message) -> None:
        """
        Команда .testcmd - отвечает "Тестовая команда работает!"
        """
        logger.info("Получена команда .testcmd")
        await utils.answer(event, self.strings['testcmd_response'])
        logger.info("Команда .testcmd обработана успешно.")

def init_module(client):
    TestModule(client)

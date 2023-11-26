"""Модуль для класса Settings."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Конфигурация бота."""
    COMMUNITY_TOKEN: str  # Токен от сообщества, который будет использовать бот
    ADMIN_TOKEN: str      # Токен юзера, который нужен для некоторых запросов
    GROUP_ID: int         # ID сообщества в ВК
    DEBUG: bool           # Режим дебага
    PREFIX: str
    CHAT_ID: int

    class Config:
        """Настройка файла .env."""
        env_file = '../../.env'
        env_file_encoding = 'utf-8'

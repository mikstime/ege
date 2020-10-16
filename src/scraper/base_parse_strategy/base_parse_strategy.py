from abc import ABC, abstractmethod
from typing import Any


class BaseParseStrategy(ABC):
    """Абстрактный класс, являющийся обёрткой для стратегии парсинга файла."""

    @abstractmethod
    def parse(self, file: str) -> Any:
        """Абстрактный метод парсинга файла
        :param str file: путь/имя файла
        :return: Any
        """
        pass

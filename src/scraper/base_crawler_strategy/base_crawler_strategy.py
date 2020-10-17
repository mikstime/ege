from typing import Any
from abc import ABC, abstractmethod


class BaseCrawlerStrategy(ABC):
    """Абстрактный класс описывабщий генератор целей для crawler."""

    @abstractmethod
    def __iter__(self) -> Any:
        """ Метод, возвращающий итератор.
        :return: Any
        """
        pass

    @abstractmethod
    def __next__(self) -> Any:
        """ Метод, возвращающий следующую цель для поиска.
        :return: Any
        """
        pass

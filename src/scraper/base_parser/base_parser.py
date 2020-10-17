from typing import Any
from abc import ABC, abstractmethod
from base_parse_strategy.base_parse_strategy import BaseParseStrategy


class BaseParser(ABC):
    """Абстрактный класс парсера необходимых значений.
    Использует BaseParseStrategy.
    """

    def __init__(self, parse_strategy: BaseParseStrategy) -> None:
        """ Конструктор
        :param BaseParseStrategy parse_strategy: Стратегия парсинга файла
        """
        self.__parse_strategy: None or BaseParseStrategy = None
        self.strategy: BaseParseStrategy = parse_strategy

    @abstractmethod
    def parse(self, file: str) -> Any:
        """ Абстрактный метод парсинга файла
        :param str file: путь/имя файла
        :return: Any
        """
        pass

    @property
    def strategy(self) -> BaseParseStrategy:
        """ Getter стратегии парсинга файла
        :return: BaseParseStrategy
        """
        return self.__parse_strategy

    @strategy.setter
    def strategy(self, parse_strategy: BaseParseStrategy) -> None:
        """ Setter стратегии парсинга файла
        :param parse_strategy: Стратегия парсинга файла
        :return: None
        """
        if not isinstance(parse_strategy, BaseParseStrategy):
            raise ValueError("Argument must be a instance of BaseParseStrategy")

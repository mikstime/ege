from abc import ABC, abstractmethod
from base_crawler_strategy.base_crawler_strategy import BaseCrawlerStrategy


class BaseCrawler(ABC):
    """Абстрактный класс, описывающий crawler (сборщик информации).
    Использует для поиска BaseCrawlerStrategy.
    """

    def __init__(self, crawler_strategy: BaseCrawlerStrategy) -> None:
        """ Конструктор класса.
        :param BaseCrawlerStrategy crawler_strategy: объект, генерирующий цели для crawler.
        """
        self.__crawler_strategy: BaseCrawlerStrategy or None = None
        self.strategy: BaseCrawlerStrategy = crawler_strategy

    @abstractmethod
    def start(self) -> None:
        """ Метод, запускающий crawler.
        :return: None
        """
        pass

    @property
    def strategy(self) -> BaseCrawlerStrategy:
        """ Getter стратегии генерации целей для поиска.
        :return: BaseCrawlerStrategy
        """
        return self.__crawler_strategy

    @strategy.setter
    def strategy(self, parse_strategy: BaseCrawlerStrategy) -> None:
        """ Setter стратегии генерации целей для поиска.
        :param parse_strategy: BaseCrawlerStrategy
        :return: None
        """
        if not isinstance(parse_strategy, BaseCrawlerStrategy):
            raise ValueError("Argument must be a instance of BaseCrawlerStrategy")
from typing import Any
from abc import ABC, abstractmethod


class BaseMathModel(ABC):
    """Абстрактный класс, описывающий математическую модель."""

    @abstractmethod
    def predict(self, context: Any) -> Any:
        """ Метод, осуществляющий работу математической модели.
        :param context: Any
        :return: Any
        """
        pass


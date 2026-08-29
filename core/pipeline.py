from abc import ABC, abstractmethod


class Pipeline(ABC):

    @abstractmethod
    def process(self, *args, **kwargs):
        pass

    
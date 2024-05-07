from abc import abstractmethod, ABC


class BaseCommand(ABC):
    @abstractmethod
    def execute(self):  # pragma: no cover
        raise NotImplementedError('Please implement in subclass')
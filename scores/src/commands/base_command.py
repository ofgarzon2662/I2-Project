from abc import abstractmethod, ABC


class BaseCommannd(ABC):
    @abstractmethod
    def execute(self):  # pragma: no cover
        raise NotImplementedError('Please implement in subclass')

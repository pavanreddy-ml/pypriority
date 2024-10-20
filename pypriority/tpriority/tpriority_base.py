from abc import ABC, abstractmethod, ABCMeta
import platform


class TPriorityBase(ABC):
    @abstractmethod
    def set_priority(self, priority):
        pass


class TPriorityMeta(ABCMeta):
    def __new__(cls, name, bases, dct):
        current_system = platform.system()

        if current_system == "Windows":
            from .windows import TPriorityWindows
            bases = (TPriorityWindows,)
        elif current_system == "Linux":
            from .unix import TPriorityUnix
            bases = (TPriorityUnix,)
        else:
            raise RuntimeError(f"Unsupported operating system: {current_system}")

        return super().__new__(cls, name, bases, dct)

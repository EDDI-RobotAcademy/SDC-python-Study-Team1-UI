import abc


class ProgramFormRepository(abc.ABC):
    @abc.abstractmethod
    def programExit(self):
        pass

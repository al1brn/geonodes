
from .scripterror import NodeError

class PropLocker:

    def _lock(self):
        self._locked = True

    def _unlock(self):
        self._locked = False

    def __setattr__(self, name, value):
        if (name not in self.__dict__) and (name not in dir(self)) and ('_locked' in self.__dict__) and self._locked:
            raise NodeError(f"Class '{type(self).__name__}' has no attribute named '{name}'", keyword=name)
        super().__setattr__(name, value)

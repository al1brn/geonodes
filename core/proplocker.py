

class PropLocker:

    def _lock(self):
        self._locked = True

    def _unlock(self):
        self._locked = False

    def __setattr__(self, name, value):
        if (name not in self.__dict__) and (name not in dir(self)) and hasattr(self, '_locked') and self._locked:
            raise AttributeError(f"{self} has no attribute named '{name}'")
        super().__setattr__(name, value)

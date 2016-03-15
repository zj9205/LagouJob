class Job:
    def __init__(self, name, pinyin):
        self.name = name
        self.pinyin = pinyin

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

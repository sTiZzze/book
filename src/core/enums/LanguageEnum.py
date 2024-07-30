from enum import Enum


class Language(Enum):
    RU = "Русский"
    EU = "English"
    PL = "Poland"
    DE = "Germany"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
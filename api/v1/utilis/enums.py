from enum import Enum


class ObjectStatus(Enum):
    new = 'new'
    accepted = 'accepted'
    rejected = 'rejected'

    @classmethod
    def choices(cls):
        return [
            (key.value, key.name)
            for key in cls
        ]


class CharacteristicTitleLn(Enum):
    rang = 'rang'
    xotira = 'xotira'
    olcham = 'o\'lcham'

    @classmethod
    def choices(cls):
        return [
            (key.value, key.name)
            for key in cls
        ]


class CharacteristicTitleKr(Enum):
    ранг = 'ранг'
    хотира = 'хотира'
    ўлчам = 'ўлчам'

    @classmethod
    def choices(cls):
        return [
            (key.value, key.name)
            for key in cls
        ]


class CharacteristicTitleRu(Enum):
    цвет = 'цвет'
    память = 'память'
    размер = 'размер'

    @classmethod
    def choices(cls):
        return [
            (key.value, key.name)
            for key in cls
        ]


class CharacteristicTitleEn(Enum):
    color = 'color'
    memory = 'memory'
    size = 'size'

    @classmethod
    def choices(cls):
        return [
            (key.value, key.name)
            for key in cls
        ]
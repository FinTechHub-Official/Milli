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

from enum import Enum


class ObjectStatus(Enum):
    new = 'new'
    accepted = 'accepted'
    rejected = 'rejected'

    @classmethod
    def choices(cls):
        return (
            (key.name, key.value)
            for key in cls
        )

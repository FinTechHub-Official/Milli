from enum import Enum


class UserRole(Enum):
    amdin = 'admin'
    client = 'client'

    @classmethod
    def choices(cls):
        return (
            (key.value, key.name)
            for key in cls
        )

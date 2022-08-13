from enum import StrEnum
from pydantic import BaseModel


class ActionName(str, StrEnum):
    pass


class FormFactor(str, StrEnum):
    pass


class ActionOverrideType(str, StrEnum):
    pass


class ActionOverride(BaseModel):
    pass

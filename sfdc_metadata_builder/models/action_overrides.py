from enum import Enum
from pydantic import BaseModel
from .base import env


class ActionName(str, Enum):
    pass


class FormFactor(str, Enum):
    pass


class ActionOverrideType(str, Enum):
    pass


class ActionOverride(BaseModel):
    def render(self):
        return env.get_template("actionOverride.xml.jinja2").render(
            **self.dict(exclude_none=True)
        )

from enum import Enum
from pydantic import BaseModel, Field
from .base import env


class ActionName(str, Enum):
    accept = "accept"
    clone = "clone"
    delete = "delete"
    edit = "edit"
    list = "list"
    new = "new"
    tab = "tab"
    view = "view"


class FormFactor(str, Enum):
    pass


class ActionOverrideType(str, Enum):
    pass


class ActionOverride(BaseModel):
    action_name: ActionName = Field(..., alias="actionOverride")

    def render(self):
        return env.get_template("actionOverride.xml.jinja2").render(
            **self.dict(exclude_none=True)
        )

    class Config:
        allow_population_by_field_name: True
        use_enum_values: True

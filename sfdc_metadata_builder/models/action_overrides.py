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
    large = "Large"
    medium = "Medium"
    small = "Small"
    null = "null"


class ActionOverrideType(str, Enum):
    default = "default"
    flexipage = "flexipage"
    lightningcompontent = "lightningcomponent"
    scontrol = "scontrol"
    standard = "standard"
    visualforce = "visualforce"


class ActionOverride(BaseModel):
    action_name: ActionName = Field(..., alias="actionName")
    form_factor: FormFactor = Field("null", alias="formFactor")
    type: ActionOverrideType = Field("default")
    skip_recordtype_select: bool = None
    comment: str = None
    content: str = None

    def render(self):
        return env.get_template("actionOverride.xml.jinja2").render(
            **self.dict(exclude_none=True)
        )

    class Config:
        allow_population_by_field_name = True
        use_enum_values = True

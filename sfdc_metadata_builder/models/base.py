from pydantic import BaseModel, Field
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("sfdc_metadata_builder"),
    autoescape=select_autoescape(),
    lstrip_blocks=True,
    trim_blocks=True,
)


class Metadata(BaseModel):
    fullname: str = Field(..., alias="fullName")
    api_version: str = "55.0"


class MetadataWithContent(Metadata):
    content: str = Field(...)


class CustomObject(Metadata):
    pass

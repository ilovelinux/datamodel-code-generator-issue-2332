# generated by datamodel-codegen:
#   filename:  products.schema.json
#   timestamp: 2025-03-03T19:42:56+00:00

from __future__ import annotations

from pydantic import BaseModel, Field

from ..commons import schema


class Products(BaseModel):
    __root__: schema.DefaultArray = Field(
        ..., description='The products in the catalog', title='Products'
    )

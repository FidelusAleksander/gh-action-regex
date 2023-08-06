from pydantic import BaseModel, Field


class ActionInput(BaseModel):
    text: str
    regex_pattern: str


class ActionOutput(BaseModel):
    match_: bool = Field(alias="match")

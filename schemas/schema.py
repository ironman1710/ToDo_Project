from pydantic import BaseModel

class Task_schema(BaseModel):
    name: str
    descriptions: str
from enum import Enum
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from uuid import UUID


class UserBaseSchema(BaseModel):
    id: Optional[UUID] = None
    first_name: str = Field(
        ..., description="The first name of the user", example="John"
    )
    last_name: str = Field(
        ..., description="The last name of the user", example="Doe"
    )
    address: Optional[str] = None
    activated: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class Status(Enum):
    Success = "Success"
    Failed = "Failed"


class UserResponse(BaseModel):
    status: Status
    user: UserBaseSchema


class GetUserResponse(BaseModel):
    status: Status
    user: UserBaseSchema


class ListUserResponse(BaseModel):
    status: Status
    results: int
    users: List[UserBaseSchema]


class DeleteUserResponse(BaseModel):
    status: Status
    message: str

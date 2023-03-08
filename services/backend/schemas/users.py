from tortoise.conrib.pydantic import pydantic_model_creator
from src.database.models import Users

# pydantic 모델 생성
# pydantic 모댈 개념

UserInSchema = pydantic_model_creator(Users,
                                      name="User",
                                      exclude_readonly=True)

UserOutSchema = pydantic_model_creator(Users,
                                       name="UserOut",
                                       exclude_readonly=True)

UsersDataBaseSchema = pydantic_model_creator(Users,
                                             name="User",
                                             exclude=["created_at", "modified_at"])
from typing import Optional # Optional : None or T
from tortoise import Tortoise

# 모델 등록

def register_tortoise(
    app,
    config:Optional[dict]=None,
    generate_schemas:bool=False,
) -> None:
    @app.on_event("startup")
    async def init_orm():
        await Tortoise.init(config=config)
        if generate_schemas:
            await Tortoise.generate_schemas()
            
    @app.on_event("shutdown")
    async def close_orm():
        await Tortoise.close_connections()


# DB 등록

# Defined the database connection via the DATABASE_URL environment variable
# Registered our models, src.database.models (users and notes) and aerich.models (migration metadata)



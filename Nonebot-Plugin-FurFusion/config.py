from pydantic import BaseSettings


class Config(BaseSettings):
    # Your Config Here
    # 插件优先级
    priority = 5

    class Config:
        extra = "ignore"

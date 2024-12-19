from pydantic import BaseModel, validator

class Config(BaseModel):
    uin: str = ""
    skey: str = ""

    @validator("uin", pre=True)
    def str_uin(cls, v):
        return str(v)  # 强制转换为字符串

    @validator("skey", pre=True)
    def str_skey(cls, v):
        return str(v)  # 强制转换为字符串

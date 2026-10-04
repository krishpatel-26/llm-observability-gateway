from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    llm_provider:str='mock'
    log_level:str='INFO'
    max_prompt_chars:int=12000
    model_config={'env_file':'.env','extra':'ignore'}
settings=Settings()

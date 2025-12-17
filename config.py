import os

class Config:
    # 替换为你的 Tushare Token
    TUSHARE_TOKEN = os.getenv("TUSHARE_TOKEN", "your_tushare_token_here")
    
    # 数据库配置 (示例)
    DB_URL = os.getenv("DB_URL", "mysql+pymysql://user:pass@localhost/quant_db")
    
    # 数据缓存目录
    CACHE_DIR = "./data_cache"

# 确保缓存目录存在
if not os.path.exists(Config.CACHE_DIR):
    os.makedirs(Config.CACHE_DIR)

import redis

def get_sync_redis():
    """Redis 동기 클라이언트 생성"""
    return redis.Redis(
        host="redis", 
        port=6379, 
        decode_responses=True
    )
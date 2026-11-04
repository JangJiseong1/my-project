import redis.asyncio as aioredis

async def get_redis_client():
    """Redis 비동기 클라이언트 생성"""
    return aioredis.from_url(
        "redis://redis:6379", 
        encoding="utf-8", 
        decode_responses=True
    )
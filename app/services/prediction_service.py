import json
import asyncio
from sqlalchemy.orm import Session
from app.core.redis_client import get_redis_client
# from app.models.prediction import PredictionResult  # 실제 프로젝트의 DB 모델 경로에 맞게 수정해, 선배!

async def process_pneumonia_prediction(db: Session, image_hash: str, model_name: str, image_path: str):
    """
    폐렴 예측 요청 처리 서비스:
    1. 동일 이미지 & 동일 모델의 결과가 DB에 캐시되어 있는지 확인
    2. 캐시가 없으면 Redis Queue에 작업을 밀어 넣고(LPUSH) Pub/Sub으로 결과 대기
    """
    
    # 1. (필수) 동일 이미지 & 동일 모델 예측 결과가 DB에 존재하는지 확인 (캐싱)
    # existing_result = db.query(PredictionResult).filter_by(
    #     image_hash=image_hash, model_name=model_name
    # ).first()
    # 
    # if existing_result:
    #     return {
    #         "status": "cached", 
    #         "prediction": existing_result.prediction, 
    #         "confidence": existing_result.confidence
    #     }

    # 2. Redis 비동기 클라이언트 연결 및 고유 Task ID 생성
    redis_client = await get_redis_client()
    task_id = f"task_{image_hash}_{int(asyncio.get_event_loop().time() * 1000)}"
    
    # 3. 결과 수신을 위한 Pub/Sub 채널 사전 구독(Subscribe)
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(f"result:{task_id}")

    try:
        # 4. Redis Task Queue('pneumonia_queue')에 작업 적재 (LPUSH)
        task_data = {
            "task_id": task_id,
            "image_path": image_path,
            "model_name": model_name
        }
        await redis_client.lpush("pneumonia_queue", json.dumps(task_data))

        # 5. Worker가 AI 추론 후 결과를 Pub/Sub으로 발행할 때까지 비동기 대기
        async for message in pubsub.listen():
            if message["type"] == "message":
                result_data = json.loads(message["data"])
                
                # 수신 완료 후 구독 해제 및 Redis 클라이언트 종료
                await pubsub.unsubscribe(f"result:{task_id}")
                await redis_client.close()
                
              
                return result_data

    except Exception as e:
        await redis_client.close()
        raise e
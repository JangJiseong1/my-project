import json
import time
import torch
from worker.redis_client import get_sync_redis

def run_worker():
    # 1. GPU가 없어도 CPU로 안전하게 동작하도록 디바이스 자동 감지 설정
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"✨ [AI Worker] initialized on device: {device}", flush=True)

    client = get_sync_redis()
    print("AI Worker Started, waiting for tasks...", flush=True)

    while True:
        try:
            # 다중 워커 환경에서 BRPOP을 이용해 대기열에서 안전하게 작업 추출
            queue_data = client.brpop("pneumonia_queue", timeout=0)
            if not queue_data:
                continue

            _, task_raw = queue_data
            task = json.loads(task_raw)
            task_id = task["task_id"]
            image_path = task["image_path"]
            model_name = task["model_name"]

            print(f"📥 [Task Received] ID: {task_id}, Model: {model_name}", flush=True)

            # 2. 폐렴 예측 모델 추론 수행 (무거운 AI 연산)
            # 예시:
            # model.to(device)
            # input_tensor = load_and_transform_image(image_path).to(device)
            # with torch.no_grad():
            #     output = model(input_tensor)

            # 임시 결과값 생성
            prediction_result = {
                "status": "success",
                "prediction": "Pneumonia Detected",
                "confidence": 0.96
            }

            # 3. 결과를 Redis Pub/Sub 채널로 발행하여 FastAPI에 전달
            client.publish(f"result:{task_id}", json.dumps(prediction_result))
            print(f"📤 [Task Completed] Result published for ID: {task_id}", flush=True)

        except Exception as e:
            error_res = {"status": "error", "message": str(e)}
            if 'task_id' in locals():
                client.publish(f"result:{task_id}", json.dumps(error_res))
            print(f"❌ [Worker Error]: {e}", flush=True)

if __name__ == "__main__":
    run_worker()
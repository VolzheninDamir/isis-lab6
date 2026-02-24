import json
import os
import redis

redis_host = os.getenv('REDIS_HOST', 'localhost')
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

CHANNEL = 'order_created'

def handle_message(message):
    """Обрабатывает полученное сообщение."""
    data = json.loads(message['data'])
    print(f"[NotificationService] Sending notification: Order {data['order_id']} for {data['customer']} "
          f"on {data['item']} (${data['amount']}) created.")

if __name__ == '__main__':
    pubsub = r.pubsub()
    pubsub.subscribe(CHANNEL)
    print(f"Notification Service subscribed to channel '{CHANNEL}'. Waiting for messages...")
    for msg in pubsub.listen():
        if msg['type'] == 'message':
            handle_message(msg)
import json
import os
import time
import random
import redis

redis_host = os.getenv('REDIS_HOST', 'localhost')
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

CHANNEL = 'order_created'

def generate_order():
    """Генерирует случайный заказ в виде словаря."""
    return {
        'order_id': random.randint(1000, 9999),
        'item': random.choice(['laptop', 'mouse', 'keyboard', 'monitor']),
        'amount': round(random.uniform(10.0, 500.0), 2),
        'customer': random.choice(['Alice', 'Bob', 'Charlie', 'Diana'])
    }

def publish_order():
    order = generate_order()
    message = json.dumps(order)
    r.publish(CHANNEL, message)
    print(f"[OrderService] Published: {order}")

if __name__ == '__main__':
    print("Order Service started. Publishing events every 5 seconds...")
    while True:
        publish_order()
        time.sleep(5)
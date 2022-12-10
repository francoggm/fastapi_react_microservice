from main import redis, Order
from time import sleep

key = 'refund_order'
group = 'payment-group'

try:
    redis.xgroup_create(key, group)
except:
    print('Group already exists!')

while True:
    try:
        results = redis.xreadgroup(group, key, {key: '>'}, None)
        if results:
            for result in results:
                obj = result[1][0][1]
                print(obj)
                try:
                    order = Order.get(obj['pk'])
                    order.status = 'refunded'
                    order.save
                except Exception as e:
                    print(e)

    except Exception as e:
        print(e)
    
    sleep(1)

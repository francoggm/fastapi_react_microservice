from main import redis, Product
from time import sleep

key = 'order_completed'
group = 'inventory-group'

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
                print(obj, Product)
                try:
                    product = Product.get(obj['product_id'])
                    print(product)
                    product.quantity -= int(obj['quantity'])
                    product.save()
                        
                except:
                    print('Sending refund event')
                    redis.xadd('refund_order', obj, '*')

    except Exception as e:
        print(e)
    
    sleep(1)

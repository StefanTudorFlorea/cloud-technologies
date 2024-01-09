import redis

# connect
r = redis.Redis(host='redis', port=6379, decode_responses=True)

# key-val
r.set('user-id', '1001')
user_id = r.get('user-id')
print('user-id: ', user_id)

# hset
r.hset('user:123', mapping={
    'name': 'sfl',
    'email': 'sfl@gmail.com',
    'age': 29
})
user = r.hgetall('user:123')
print(user)
import redis

# connect
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# key-val
r.set('user-id', '1001')
user_id = r.get('user-id')
print('user-id: ', user_id)

# hset
r.hset('user:123', mapping= {
    'name': 'sfl',
    'email': 'sfl@gmail.com',
    'age': 29
})
user = r.hgetall('user:123')
print(user)

# pipeline
userA = { 'name': 'userA', 'age': 10 }
userB = { 'name': 'userA', 'age': 10 }
userC = { 'name': 'userA', 'age': 10 }

pipe = r.pipeline()
pipe.hset('users#userA', mapping=userA)
pipe.hset('users#userB', mapping=userA)
pipe.hset('users#userC', mapping=userA)
pipe.execute()

pipe = r.pipeline()
pipe.hgetall('users#userA')
pipe.hgetall('users#userB')
pipe.hgetall('users#userC')
result = pipe.execute()
print(f'pipeline result: {result}')
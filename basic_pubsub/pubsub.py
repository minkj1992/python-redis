"""Basic pubsub model with redis-py

$ python pubsub.py
    # mozzart_reids == music_redis?
    Redis<ConnectionPool<Connection<host=localhost,port=6379,db=0>>>
    Redis<ConnectionPool<Connection<host=localhost,port=6379,db=0>>>
    False
    # must be ignored!
    {'type': 'subscribe', 'pattern': None, 'channel': b'classical_music', 'data': 1}
    # new music, new_music['data]
    {'type': 'message', 'pattern': None, 'channel': b'classical_music', 'data': b'mozzart music'}
    b'mozzart music'
    # another new music, another new music['data]
    {'type': 'message', 'pattern': None, 'channel': b'classical_music', 'data': b'mozzart music2'}
    b'mozzart music2'

"""
import redis

MUSIC_CATEGORY = {
    "CLASSIC": 'classical_music',
    "HIPHOP": 'hiphop-music',
    "KPOP":'k-pop-music'
}

music_redis = redis.Redis(host='localhost', port=6379, db=0)
music_pub_sub = music_redis.pubsub()
# subscribe to classical music
music_pub_sub.subscribe(MUSIC_CATEGORY["CLASSIC"])


mozzart_redis = redis.Redis(host='localhost', port=6379, db=0)
mozzart_redis.publish(MUSIC_CATEGORY["CLASSIC"], "mozzart music")

print("# mozzart_reids == music_redis?")
print(mozzart_redis)
print(music_redis)
print(mozzart_redis == music_redis)

print("# must be ignored!")
tmp = music_pub_sub.get_message()
print(tmp)

print("# new music, new_music['data]")
new_music = music_pub_sub.get_message()
print(new_music)
print(new_music['data'])


print("# another new music, another new music['data]")
mozzart_redis.publish(MUSIC_CATEGORY["CLASSIC"], "mozzart music2")
another_music = music_pub_sub.get_message()
print(another_music)
print(another_music['data'])
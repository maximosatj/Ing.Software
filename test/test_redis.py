# import unittest
# import redis

# class RedisTestCase(unittest.TestCase):
#     def setUp(self):
#         self.redis = redis.Redis(host='redis',db=0, port=6379, password='maximo')

#     def test_redis_set_get(self):
#         self.redis.set('test', 'value')
#         value = self.redis.get('test')
#         self.assertEqual(value, b'value')

# if __name__ == '__main__':
#     unittest.main()

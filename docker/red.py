import redis

conn = redis.Redis("localhost")

user = {"Name": "Pradeep", "Company": "SCTL", "Address": "Mumbai", "Location": "RCP"}

conn.hmset("pythonDict", user)

dd = conn.hgetall("pythonDict")
print(dd)

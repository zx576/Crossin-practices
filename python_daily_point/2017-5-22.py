

import pymongo


client = pymongo.MongoClient()
db = client.gradcafe
db_info = db.info


# db_info.remove()

count = 0
for i in db_info.find():
    count += 1


print(count)

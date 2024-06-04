from app.model.connection import mongodb

client = mongodb.get_client()
db = client['hellody']

async def season_detail(series_id):
    collection = db['SEASON']
    cursor = collection.find({'SERIES_ID': series_id}, {'_id': 0, 'SEASON_ID': 1, 'SEASON_NUM':1}).sort({'SEASON_NUM':1})
    vod_list = await cursor.to_list(length=100)
    print(vod_list)
    return vod_list
    
from models import Pet, db
from app import app

db.drop_all()
db.create_all()

bob = Pet(
    name='Bob', 
    species='chicken', 
    photo_url='https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/f_auto,q_auto,w_1100/v1555930041/shape/mentalfloss/istock_000006350265-chicken_6.jpg',
    age=1,
    notes='oof',
)
sally = Pet(
    name='Sally', 
    species='cat', 
    photo_url='https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/cat_relaxing_on_patio_other/1800x1200_cat_relaxing_on_patio_other.jpg',
    age=3,
    notes='a pretty girl',
)
simba = Pet(
    name='Simba', 
    species='lion', 
    photo_url='https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/1200px-Lion_waiting_in_Namibia.jpg',
    age=5,
    notes='rawr',
)

db.session.add_all([bob, sally, simba])
db.session.commit()
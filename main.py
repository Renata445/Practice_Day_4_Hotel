import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017/")
current_db = db_client["hotel"]

collection = current_db["guests"]

it_guests = [
    {'id': '1', 'passport': '9216234576', 'check_in': '12.03.2020', 'check_out': '23.03.2020', 'surname': 'Mandarinova', 'name': 'Dasha', 'room_id': '3'},
    {'id': '2', 'passport': '9213569845', 'check_in': '29.03.2020', 'check_out': '01.04.2020', 'surname': 'Olegrova', 'name': 'Marina', 'room_id': '12'},
    {'id': '3', 'passport': '9256789045', 'check_in': '13.05.2020', 'check_out': '23.05.2020', 'surname': 'Rulakov', 'name': 'Oleg', 'room_id': '22'},
    {'id': '4', 'passport': '9203145678', 'check_in': '16.07.2020', 'check_out': '12.09.2020', 'surname': 'Gorilov', 'name': 'Andrey', 'room_id': '11'},
    {'id': '5', 'passport': '9214789032', 'check_in': '02.11.2020', 'check_out': '01.02.2021', 'surname': 'Purinova', 'name': 'Elena', 'room_id': '6'}

]
result = collection.insert_many(it_guests)



from pymongo import MongoClient, errors
from bson.objectid import ObjectId

# Підключення до MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['cat_database']
collection = db['cats']

def create_cat(name, age, features):
    """Створює нового кота в базі даних"""
    try:
        cat = {
            "name": name,
            "age": age,
            "features": featuresx
        }
        result = collection.insert_one(cat)
        print(f"Кіт створений з ID: {result.inserted_id}")
    except errors.PyMongoError as e:
        print(f"Помилка при створенні кота: {e}")

def read_all_cats():
    """Виводить всі записи з колекції"""
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except errors.PyMongoError as e:
        print(f"Помилка при зчитуванні котів: {e}")

def read_cat_by_name(name):
    """Виводить інформацію про кота за ім'ям"""
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кіт з ім'ям {name} не знайдений")
    except errors.PyMongoError as e:
        print(f"Помилка при зчитуванні кота: {e}")

def update_cat_age(name, new_age):
    """Оновлює вік кота за ім'ям"""
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print(f"Вік кота з ім'ям {name} оновлено")
        else:
            print(f"Кіт з ім'ям {name} не знайдений")
    except errors.PyMongoError as e:
        print(f"Помилка при оновленні віку кота: {e}")

def add_feature_to_cat(name, feature):
    """Додає нову характеристику до списку features кота за ім'ям"""
    try:
        result = collection.update_one({"name": name}, {"$addToSet": {"features": feature}})
        if result.modified_count > 0:
            print(f"Характеристика додана до кота з ім'ям {name}")
        else:
            print(f"Кіт з ім'ям {name} не знайдений або характеристика вже існує")
    except errors.PyMongoError as e:
        print(f"Помилка при додаванні характеристики: {e}")

def delete_cat_by_name(name):
    """Видаляє запис з колекції за ім'ям тварини"""
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кіт з ім'ям {name} видалений")
        else:
            print(f"Кіт з ім'ям {name} не знайдений")
    except errors.PyMongoError as e:
        print(f"Помилка при видаленні кота: {e}")

def delete_all_cats():
    """Видаляє всі записи з колекції"""
    try:
        result = collection.delete_many({})
        print(f"Всі коти видалені, видалено {result.deleted_count} записів")
    except errors.PyMongoError as e:
        print(f"Помилка при видаленні всіх котів: {e}")

if __name__ == "__main__":
    # Приклади використання функцій
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    read_all_cats()
    read_cat_by_name("barsik")
    update_cat_age("barsik", 4)
    add_feature_to_cat("barsik", "любит гратися")
    delete_cat_by_name("barsik")
    delete_all_cats()

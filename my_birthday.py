import datetime

def my_birthday(birthday):
    today = datetime.date.today()
    return (birthday - today).days

if __name__ == '__main__':
    print(my_birthday(datetime.date(2024,3,7)))

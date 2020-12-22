import os

db = os.path.join(os.path.dirname(__file__), "file_6.txt")
db_dict = {}
with open(db, "r", encoding='utf-8') as file:
    for line in file:
        tmp = line.split(" ")
        less = tmp[0].split(":")[0]
        db_dict[less] = tmp[1:]

result = {}
for key, value in db_dict.items():
    result[key] = sum([int(itm.split('(')[0]) for itm in value if itm.split('(')[0].isdigit()])

print(result)

# закопипастил код, но с разбором!!

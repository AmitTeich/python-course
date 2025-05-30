from datetime import datetime,date

#Ex.1
def db_open(filename):
    f = open(filename)
    header = next(f).strip().split(',')
    return header, f

#Ex.1 record
def db_create_record(keys, filehandler):
    rec = {}
    line = next(filehandler).strip().split(',')
    rec = {keys[i]: line[i] for i in range(len(keys))}
    return rec

#Ex.2
def db_print_record(keys, record):
    for key in keys:
        print("   ", end='')
        print(f"{key:<15}      = {record[key]}" )

#Ex.3
def db_print(file, n):
    header, f = db_open(file)
    for k in range(n):
        print(f"record {k+1}:")
        rec = db_create_record(header, f)
        db_print_record(rec.keys(), rec)
    f.close()


#Preliminary question to question 4
def db_create_list_of_record(file, n):
    header, f = db_open(file)
    records = []
    try:
        for k in range(n):
            rec = db_create_record(header, f)
            records.append(rec)
    except StopIteration:
        pass
    f.close()
    return records, header


#Ex.4
def db_save(keys, records, file):
     f= open(file,'w')
     f.write(f"{",".join(keys)}\n")
     for record in records:
         f.write(f"{",".join(record[key] for key in keys)}\n")
     f.close()

#Ex.5
def find_age(birthday):
    birth_date = datetime.strptime(birthday, "%m/%d/%Y").date()
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age-=1
    return age

#Ex.6
def db_query1(filename):
    records, header = db_create_list_of_record(filename,999999)
    counter =0
    for record in records:
        if record["State"] == "FL" and find_age(record["Birthday"]) > 32 :
            counter+= 1
    return counter

#Ex.7
def db_query2(dbfile, filename):
    good_records = []
    records, header = db_create_list_of_record(dbfile, 999999)
    for record in records:
        if record["Gender"] == "female":
            if record["State"] == "OH" or record["State"] == "CA":
                if find_age(record["Birthday"]) < 45:
                    if record["BloodType"] == "B+":
                        record["Age"] = str(find_age(record["Birthday"]))
                        good_records.append(record)
    keys = ["GivenName", "Surname", "NationalID","Age", "Birthday", "TelephoneNumber", "EmailAddress"]
    db_save(keys, good_records, filename)





#db_print('db.csv',3)
#header, f = db_open('db.csv')
#rec = db_create_record(header,f)
#db_print_record(rec.keys(),rec)
#records, header = db_create_list_of_record('db.csv',999)
#db_save(header,records,'new_data.csv')
#age = find_age(records[0]["Birthday"])
#print(age)
#print(db_query1('db.csv'))
#db_query2('db.csv',"Table2.csv")


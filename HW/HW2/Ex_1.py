import re

def extract_israel_districts(filename):
    f = open(filename,encoding="utf-8" )
    header = next(f).strip().split(',')
    results=list()
    for line in f:
        row=line.strip().split(',')
        if row[2] == 'IL':
            results.append([row[1],row[0]])
    write_to_csv('districs.csv', results, "District name,Code")
    f.close()

def extract_all_districts(filename):
    f = open(filename,encoding="utf-8")
    header = next(f).strip().split(',')
    results = list()
    for line in f:
        row=line.strip().split(',')
        if  re.search(r'\bDistrict\b',row[1]) and re.search(r'^[AO]',row[1]):
            results.append([row[3], row[1]])
    write_to_csv('All_dist.csv', results, "Country Name,State Name")
    f.close()


def write_to_csv(filename, l, header):
    f=open(filename,'w',encoding="utf-8")
    f.write(f"{header}\n")
    for i in l:
        f.write(f"{','.join(i)}\n")
    f.close()




def main():
    extract_israel_districts("states_by_country.csv")
    extract_all_districts("states_by_country.csv")


if __name__ == '__main__':
    main()

import csv, sqlite3

hots_db = r'C:\Users\baxter\reader\apps\Hots\hots_data.db'
hero_file = r'C:\Users\baxter\reader\apps\Hots\hero_data.csv'
map_file = r'C:\Users\baxter\reader\apps\Hots\hots_data.csv'
file_list = [map_file, hero_file]
file_dict = {map_file: 'map_name', hero_file: 'hero_name'}
table_name_dict = {map_file: 'map_data', hero_file: 'hero_data'}
conn = sqlite3.connect(hots_db)
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS hero_data (hero_name VARCHAR PRIMARY KEY, waveclear INT, dmg_sustain INT, dmg_burst INT, tank INT, cc INT, support_sustain INT, support_save INT)')
c.execute('CREATE TABLE IF NOT EXISTS map_data (map_name VARCHAR PRIMARY KEY, waveclear INT, dmg_sustain INT, dmg_burst INT, tank INT, cc INT, support_sustain INT, support_save INT)')

for file in file_list:
    with open(file, 'rt') as fn:
        dr = csv.DictReader(fn)
        to_db = [(row[file_dict[file]], row['waveclear'], row['dmg_sustain'], row['dmg_burst'], row['tank'], row['cc'], row['support_sustain'], row['support_save']) for row in dr]
    str_query = 'INSERT INTO {} ({}, waveclear, dmg_sustain, dmg_burst, tank, cc, support_sustain, support_save) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'.format(table_name_dict[file], file_dict[file])
    print(str_query)
    c.executemany(str_query, to_db)

conn.commit()
conn.close()

from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

print(apps_data[:1])

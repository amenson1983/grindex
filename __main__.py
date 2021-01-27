
import csv


if __name__ == '__main__':
    with open("itemprices.csv", "r", encoding="UTF", newline="") as file:
        reader = csv.reader(file,delimiter=';')
        dictionary1 = []
        for row in reader:
            row[1] = row[1].replace(',','.')
            print(row[0], row[1])
            dictionary1.append({row[0]:row[1]})
    dictionary = dictionary1[1:]
    print(dictionary[:])
    new_dict = {}
    for item in dictionary:
        new_dict.update(item)
    print(new_dict, '\n',new_dict.get('Аксастрол'))
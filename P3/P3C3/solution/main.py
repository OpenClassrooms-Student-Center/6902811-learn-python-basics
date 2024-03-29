import csv

def extract():
    data = []
    with open('input.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            data.append(line)
    return data

def transform(data_to_transform):
    data_to_load = []
    for data in data_to_transform:
        transformed_data = {}
        transformed_data["name"] = data["name"]
        data["hours_worked"] = int(data["hours_worked"]) * 15
        transformed_data["salary"] = str(data["hours_worked"])
        data_to_load.append(transformed_data)
    return data_to_load

def load(data_to_load):
    with open('output.csv', mode='w') as file:
        fieldnames = ['name', 'salary']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for data in data_to_load:
            writer.writerow(data)

def main():
    data_to_transform = extract()
    data_to_load = transform(data_to_transform)
    load(data_to_load)


if __name__ == "__main__":
    main()
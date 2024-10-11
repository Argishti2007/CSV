import csv

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        print("Содержимое файла:")
        for row in reader:
            print(f"First Name: {row['first_name']}, Last Name: {row['last_name']}, Address: {row['address']}")

def filter_by_first_name(file_path, name_filter):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        print(f"\nФильтрация по имени '{name_filter}':")
        for row in reader:
            if row['first_name'].lower() == name_filter.lower():
                print(f"First Name: {row['first_name']}, Last Name: {row['last_name']}, Address: {row['address']}")

if __name__ == "__main__":
    file_path = 'name.csv' 
    
    read_csv(file_path)
    
    name_filter = input("\nВведите имя для фильтрации: ")  
    if name_filter:
        filter_by_first_name(file_path, name_filter)

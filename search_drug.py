import json

# Hàm tải dữ liệu từ file JSON
def load_data():
    with open('drugs.json', 'r') as file:
        return json.load(file)

# Hàm tìm kiếm thuốc theo tên
def search_drug(drugs, name):
    for drug in drugs:
        if drug['name'].lower() == name.lower():
            return drug
    return None

# Chạy chương trình
if __name__ == "__main__":
    drugs = load_data()
    name = input("Enter drug name to search: ")
    result = search_drug(drugs, name)

    if result:
        print(f"\nDrug Found:\n"
              f"Name: {result['name']}\n"
              f"Ingredient: {result['ingredient']}\n"
              f"Usage: {result['usage']}\n"
              f"Form: {result['form']}")
    else:
        print("Drug not found.")

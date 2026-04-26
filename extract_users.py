import openpyxl
import json

def extract_data(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    data = []
    # Assuming the first row is header and column 1 is ID, column 2 is Name
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[0] and row[1]:
            data.append({"id": str(row[0]).strip(), "name": str(row[1]).strip()})
    return data

if __name__ == "__main__":
    users = extract_data("user_no_name.xlsx")
    print(json.dumps(users, ensure_ascii=False))

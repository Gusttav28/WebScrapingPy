from openpyxl import Workbook

def createdFile():
    wb = Workbook()
    sheet = wb.active
    sheet['A1'] = 'Name'
    wb.save("exceltest.xlsx")


if __name__ == "__main__":
    createdFile()
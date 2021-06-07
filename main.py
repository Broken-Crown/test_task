import openpyxl
import time
import random
from pathlib import Path


_COMPANY_NAME = ["Компания_1", "Компания_2", "Компания_3"]
_OPERATIONS = ["Выплата зп", "Отплата налогов", "Закупка оборудования"]
_TABLE_HEADER = ["Компания", "Дата", "Тип операции", "Сумма"]
_CUSTOM_FIRST_TABLE_PATH = Path(r".\first_table.xlsx")
_CUSTOM_SECOND_TABLE_PATH = Path(r".\second_table.xlsx")

def create_table():
	wb = openpyxl.Workbook()
	ws = wb.active
	ws.title = "Информация по операциям"
	

	for index, cell in enumerate(ws.iter_cols(max_row = 1, max_col = len(_TABLE_HEADER))):
		cell[0].value = _TABLE_HEADER[index]

	wb.save(_CUSTOM_FIRST_TABLE_PATH)

if __name__ == "__main__":
	print("Опять работать?")
	create_table()
	print("Дело сделано!")

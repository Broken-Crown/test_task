from datetime import datetime, timedelta
from pathlib import Path
import openpyxl
import random


_TABLE_INFORMATION: dict[str, tuple] = {
    "Header": ("Компания", "Дата", "Тип операции", "Сумма"),
    "Company_name": ("Компания_1", "Компания_2", "Компания_3"),
    "Operations": ("Выплата зп", "Отплата налогов", "Закупка оборудования")
}

_CUSTOM_FIRST_TABLE_PATH: Path = Path(r".\first_table.xlsx")
_CUSTOM_SECOND_TABLE_PATH: Path = Path(r".\second_table.xlsx")
_MAX_ROW_NUMBER: int = 10000
_MAX_COL_NUMBER: int = len(_TABLE_INFORMATION["Header"])


def create_table(save_path: Path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Информация по операциям"

    ws.append(_TABLE_INFORMATION["Header"])

    current_date = datetime.now()
    current_row_number: int = 1

    while current_row_number < _MAX_ROW_NUMBER:
        date_string: str = f"{current_date.year}-{current_date.month:02}-{current_date.day:02} " \
            f"{current_date.hour:02}:{current_date.minute:02}:{current_date.second:02}"

        current_row: tuple[str, str, str, int] = (
            random.choice(_TABLE_INFORMATION["Company_name"]),
            date_string,
            random.choice(_TABLE_INFORMATION["Operations"]),
            random.randint(100, 500000)
        )

        ws.append(current_row)

        current_date += timedelta(seconds=random.randint(0, 10))
        current_row_number += 1

    wb.save(save_path)


if __name__ == "__main__":
    print("Опять работать?")
    for save_path in [_CUSTOM_FIRST_TABLE_PATH, _CUSTOM_SECOND_TABLE_PATH]:
        create_table(save_path)
    print("Дело сделано!")

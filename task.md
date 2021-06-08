# Тестовое задание

## 1. Слияние файлов
Имеются два файла с операциями в формате XLSX,
пример данных:

`Компания_2	2021-06-08 11:44:09	Закупка оборудования	343219`

Соответственно, в каждом файле 4 колонки:
* компания;
* дата;
* тип операции;
* сумма.

Требуется написать программу для объединения этих
файлов с сортировкой по колонке "Дата".

К заданию прилагается вспомогательный скрипт на
python3, который создает два файла "first_table.xlsx" и
"second_table.xlsx".

## 2. Пользовательский интерфейс

С помощью pyside2 необходимо создать работающий 
пользовательский интерфейс для программы.

В интерфейсе должны присутствовать следующие элементы:
* поля ввода адресов файлов;
* кнопка начала программы.

## 3. Дополнительные параметры

В рамках дополнительного задания необходимо
реализовать следующий функционал:
* чекбокс для исключения какого-либо столбца из 
  итогового файла со строкой, в которую можно 
  вписать название исключаемого столбца;
* поле ввода для указания максимального количества 
  строк в итоговом документе;
* чекбокс или любой другой способ для настройки
  опций сортировки (сортировать по дате, компании...)
  
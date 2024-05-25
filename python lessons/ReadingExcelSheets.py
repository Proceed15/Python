#a
Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/José/Desktop/python lessons/ReadingExcelSheets.py
import pandas as pd
file = pd.ExcelFile("/Users/José/Desktop/Sales.xlsx")
Traceback (most recent call last):
  File "C:\Users\José\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\compat\_optional.py", line 135, in import_optional_dependency
    module = importlib.import_module(name)
  File "C:\Users\José\AppData\Local\Programs\Python\Python311\Lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1140, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'openpyxl'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    file = pd.ExcelFile("/Users/José/Desktop/Sales.xlsx")
  File "C:\Users\José\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\excel\_base.py", line 1567, in __init__
    self._reader = self._engines[engine](
  File "C:\Users\José\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\excel\_openpyxl.py", line 552, in __init__
    import_optional_dependency("openpyxl")
  File "C:\Users\José\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\compat\_optional.py", line 138, in import_optional_dependency
    raise ImportError(msg)
ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.
file = pd.ExcelFile("/Users/José/Desktop/Sales.xlsx")
print(file.sheet_names)
['Planilha1']
sheet = file.parse('planilha1')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sheet = file.parse('planilha1')
  File "C:\Users\José\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\excel\_base.py", line 1616, in parse
    return self._reader.parse(
  File "C:\Users\José\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\excel\_base.py", line 773, in parse
    sheet = self.get_sheet_by_name(asheetname)
  File "C:\Users\José\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\excel\_openpyxl.py", line 582, in get_sheet_by_name
    self.raise_if_bad_sheet_by_name(name)
  File "C:\Users\José\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\io\excel\_base.py", line 624, in raise_if_bad_sheet_by_name
    raise ValueError(f"Worksheet named '{name}' not found")
ValueError: Worksheet named 'planilha1' not found
sheet = file.parse('Planilha1')
print(sheet)
        Data             Customer  Invoice   Amount
0 2018-12-01  Start Brothers Inc.       98  1340.00
1 2018-12-10             MMC Inc.       99  1900.00
2 2018-12-12             MMC Inc.      100  2900.00
3 2018-12-14  Start Brothers Inc.      101   977.99
4 2018-12-21     Steel & Iron LLC      102  3400.00
type(sheet)
<class 'pandas.core.frame.DataFrame'>
print(sheet.Data)
0   2018-12-01
1   2018-12-10
2   2018-12-12
3   2018-12-14
4   2018-12-21
Name: Data, dtype: datetime64[ns]
sheet.Amount.sum()
10517.99
sheet.loc[0]
Data        2018-12-01 00:00:00
Customer    Start Brothers Inc.
Invoice                      98
Amount                   1340.0
Name: 0, dtype: object
sheet.loc[0, "Amount"]
1340.0
sheet.set_index("Customer", inplace=True)
sheet.loc["MMC Inc."]
               Data  Invoice  Amount
Customer                            
MMC Inc. 2018-12-10       99  1900.0
MMC Inc. 2018-12-12      100  2900.0
sheet = sheet.reset_index()
sheet["Invoice"]
0     98
1     99
2    100
3    101
4    102
Name: Invoice, dtype: int64
type(sheet)
  
<class 'pandas.core.frame.DataFrame'>
type(sheet["Invoice"])
<class 'pandas.core.series.Series'>
sheet.loc[ sheet["Invoice"] == 99 ]
   Customer       Data  Invoice  Amount
1  MMC Inc. 2018-12-10       99  1900.0
sheet.loc[ sheet["Amount"] > 2000 ]
           Customer       Data  Invoice  Amount
2          MMC Inc. 2018-12-12      100  2900.0
4  Steel & Iron LLC 2018-12-21      102  3400.0
sheet.loc[ sheet["Amount"].idmax() ]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    sheet.loc[ sheet["Amount"].idmax() ]
  File "C:\Users\José\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\generic.py", line 6296, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'idmax'. Did you mean: 'idxmax'?
sheet.loc[ sheet["Amount"].idxmax() ]
Customer       Steel & Iron LLC
Data        2018-12-21 00:00:00
Invoice                     102
Amount                   3400.0
Name: 4, dtype: object
sheet.loc[ sheet["Amount"].idxmax() ]["Customer"]
'Steel & Iron LLC'
sheet.loc[ sheet["Amount"] > 1800 ]
           Customer       Data  Invoice  Amount
1          MMC Inc. 2018-12-10       99  1900.0
2          MMC Inc. 2018-12-12      100  2900.0
4  Steel & Iron LLC 2018-12-21      102  3400.0
sheet.loc[ sheet["Amount"] > 1800 ]["Customer"]
1            MMC Inc.
2            MMC Inc.
4    Steel & Iron LLC
Name: Customer, dtype: object
sheet.loc[ sheet["Amount"] > 1800 ]["Customer"].unique()
array(['MMC Inc.', 'Steel & Iron LLC'], dtype=object)
sheet.loc[ sheet["Amount"] > 1800 ]["Customer"].unique()[0]
'MMC Inc.'
for customer in sheet.loc[ sheet["Amount"] > 1800 ]["Customer"].unique(): print(customer)
for customer in sheet.loc[ sheet["Amount"] > 1800 ]["Customer"].unique(): print(customer)
SyntaxError: invalid syntax
for customer in sheet.loc[ sheet["Amount"] > 1800 ]["Customer"].unique(): print(customer)

MMC Inc.
Steel & Iron LLC

#Press Enter to execute the for, the last command on this file.

import sys
import pandas as pd
import self as self

from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from pandas import ExcelWriter, DataFrame

#pizza_result = pd.read_excel("pizzaInfo.xlsx", sheet_name="Sheet1")
#pizza_tem = pd.read_excel("pizzaInfo.xlsx", sheet_name="Sheet2")

df1 = pd.DataFrame.from_records([{'날짜': '2020-11-30', '메뉴': '피자', '개수': 1, '가격': 3500}])
df2 = pd.DataFrame.from_records([{'날짜': '2020-11-30', '메뉴': '피자', '개수': 1, '가격': 3500}])

with ExcelWriter('path_to_file.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')


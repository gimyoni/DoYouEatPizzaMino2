import pandas as pd
from PySide2.QtCore import QDate, Qt

df = pd.read_excel("pizzaInfo.xlsx", sheet_name = "Sheet1")

df = df.sort_values(by=['가격'], ascending=[False])
date = QDate.currentDate()

new_row = {'날짜':date.toString(Qt.ISODate), '메뉴':'직화 스테이크', '개수':1, '가격':33900}

df = df.append(new_row, ignore_index=True)
print(df)

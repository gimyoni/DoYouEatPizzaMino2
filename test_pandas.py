import sys
import pandas as pd
from PySide2.QtCore import QRect
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QLabel
from matplotlib import pyplot
from pandas import DataFrame
from pandas import read_excel
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
    # 윈도우인 경우
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:
    # Mac 인 경우
    rc('font', family='AppleGothic')

matplotlib.rcParams['axes.unicode_minus'] = False
# 그래프에서 마이너스 기호가 표시되도록 하는 설정입니다.

def makePlot():
    pizza_data = pd.read_excel("pizzaInfo.xlsx", sheet_name="Sheet3")
    pizzatmp = pizza_data.filter(['메뉴','개수'])
    pizzadf = pizzatmp.groupby(['메뉴']).sum()
    print(pizzadf)

    pizza = DataFrame(pizzadf, columns=['개수'])
    pizza['개수'].plot.pie()

    pyplot.title("인기메뉴를 알려드립니다^0^")

    pyplot.ylabel(None)

    pyplot.savefig("plot.png", bbox_inces='tight', pad_inches=0)

    pyplot.close()


#
# from PySide2 import QtCore
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *
# from pandas import ExcelWriter, DataFrame
#
# #pizza_result = pd.read_excel("pizzaInfo.xlsx", sheet_name="Sheet1")
# #pizza_tem = pd.read_excel("pizzaInfo.xlsx", sheet_name="Sheet2")
#
# df1 = pd.DataFrame.from_records([{'날짜': '2020-11-30', '메뉴': '피자', '개수': 1, '가격': 3500}])
# df2 = pd.DataFrame.from_records([{'날짜': '2020-11-30', '메뉴': '피자', '개수': 1, '가격': 3500}])
#
# with ExcelWriter('path_to_file.xlsx') as writer:
#     df1.to_excel(writer, sheet_name='Sheet1')
#     df2.to_excel(writer, sheet_name='Sheet2')

# with open('nowPizzaCart.txt') as file:
#   for line in file.readlines():
#     result = line.strip().split('\t')
#     for r in result:
#         print(r)
#ФАЙЛ DB_P.py ДОЛЖЕН ОТСУТСТВОВАТЬ В КАТАЛОГЕ!!!!
#ЗАПУСКАТЬ СКРИПТ КОМАНДОЙ "python OS_Python_Create_IMG.py" 
import numpy as np
from matplotlib import pyplot as plt
import pytest
import sys,subprocess,os
from sys import platform
decode_text=""
if platform == "linux" or platform == "linux2" or platform == "darwin":# linux or MacOS
    decode_text="utf-8"
elif platform == "win32":
    decode_text="1251"
color_mas=['b','g','r','c','m','y','k']
linestyle_mas=['-',':','--','-.']
# В Var_mas конфигурация вариантов такова:
# 1-е число-это индекс цвета линии из массива color_mas(начинается с нуля);
# 2-е число-это толщина линии графика(число типа float);
# 3-е число-это какой тип линии из массива linestyle_mas(начинается с нуля);
# Пример: [1,2,0],где 1-'g',т.е. зеленый цвет линии;2-толщина линии 2;0-'-',т.е. тип линии сплошной
Var_mas=[[0,2,0],[1,3,1],[2,5,2],[3,4,3],[4,5,0],
         [5,3,1],[6,2,2],[0,6,3],[1,6,0],[2,2,1],
         [3,4,2],[4,3,3],[5,5,0],[3,6,1],[0,4,2],
         [1,4,3],[2,6,0],[3,5,1],[4,2,2],[5,7,3],
         [6,3,0],[0,2,1],[1,3,2],[2,5,3],[3,2,0]]

#Генерация списка вариантов графиков
def Generate_var_list():     
  color_text=['Синий','Зеленый','Красный','Голубой','Пурпурный','Желтый','Черный']
  linestyle_text=['Сплошной','Точечный','Пунктирный','Пунктирно-точечный']
  with open('Var_list.txt','w',encoding=decode_text) as f:
    f.write("Характеристики линий\n")
    for i in range(0,25):
        color_=color_text[Var_mas[i][0]]
        linewidth_=Var_mas[i][1]
        linestyle_=linestyle_text[Var_mas[i][2]]
        if i<9:
            f.write(str(i+1)+".  цвет:"+color_+", толщина:"+str(linewidth_)+", тип:"+linestyle_+"\n")
        else:
            f.write(str(i+1)+". цвет:"+color_+", толщина:"+str(linewidth_)+", тип:"+linestyle_+"\n")
    f.close()



try:#Проверка на то, является ли этот скрипт первым(главным),т.е. что отсутствует файл DB_P.py
    f = open('DB_P.py','r')
except IOError as e:
    with open('DB_P.py','w',encoding=decode_text) as f:
      f.write("task_id="+str(-1)+"\n")
      f.close()
else:
    f.close()

from DB_P import task_id
if task_id ==-1:
  for i in range(1,25+1):
    with open('DB_P.py','w',encoding=decode_text) as f:
      f.write("task_id="+str(i)+"\n")
      f.close()
    c=subprocess.run("pytest --mpl-generate-path=baseline OS_Python_Create_IMG.py", shell=True,capture_output=True)
    tmp =c.stdout.decode(decode_text)#'utf-8')
    print(tmp)
  #Генерация списка вариантов графиков
  Generate_var_list()

if task_id==25:# удаление файла
  os.remove('DB_P.py') 
a=0
b=0
c=0
d=0
x = []
y=[]
if task_id == 1:
  a = 3
  b = 2
  c = 4
  d = 1
  x = np.linspace(-10, 10, 100)
  y = a * x ** 5 + b * x ** 2 + c * x + d
elif task_id == 2:
  a = 2
  b = 2
  c = 3
  x = np.linspace(0, 10, 100)
  y = a*np.sin(b*x+c)
elif task_id == 3:
  a = 2
  b = 2
  c = 2
  x = np.linspace(0, 10, 100)
  y = np.tan(a*x**2 + b*x + c)
elif task_id == 4:
  a = 12
  b = 2
  c = 8
  x = np.linspace(0, 10, 100)
  y = a * np.log(b+c * x)
elif task_id == 5:
  a = 5
  b = 100000
  c = 2
  x = np.linspace(0, 10, 25)  
  y = a * np.log(x/(b+c*x))
elif task_id == 6:
  a = 100000
  b = 10000
  c = 2
  d = 8
  x = np.linspace(-100, 100, 100)
  y = np.log(a*x**2 + b*x + c)/np.log(d)
elif task_id == 7:
  a = 0.5
  b = 1
  c = -3
  d = 0.5
  x = np.linspace(-8, 6, 100)
  y = d ** (a * x ** 2 + b * x + c)
elif task_id == 8:
  a = 2
  b = 3
  c = 5
  d = 6
  x = np.linspace(0, 100, 1000)
  y = np.log(np.log(c*x+d)/np.log(b))/np.log(a)
elif task_id == 9:
  a = 1.5
  b = 2
  c = -5
  x = np.linspace(0, 10, 100)
  y = 1/a*np.log(abs(b*x+c))
elif task_id == 10:
  a = 3
  b = 4
  c = 2
  d = 7
  x = np.linspace(0, 2*np.math.pi, 100)
  y = a * np.sin(b*x) + c * np.sin(d*x)
elif task_id == 11:
  a = 6
  b = 2
  x = np.linspace(0, 100, 1000)
  y = a*(x**2)*np.sin(b*x)
elif task_id == 12:
  a = 5
  b = 3
  c = -1
  x = np.linspace(1, 20, 200)
  y = a * np.sin(b*x)/x + c
if task_id == 13:
  a=1
  b=2
  c=3
  x = np.arange(0, 2*np.math.pi, 0.1)
  y = np.sqrt((np.square(c) - a * x **2)/ b)
elif task_id == 14:
  x = np.linspace(-2.1,2.1, 1000)
  y1 = (1 - (1 - abs(x)) ** 2) ** 0.5  
  y2 = np.arccos(1-abs(x))-np.pi
  y = np.column_stack((y1,y2))
elif task_id == 15:
  a = 2
  b = 3
  c = -2
  d = 2
  x = np.linspace(-10, 10, 100)
  y = a * x ** 3 + b * x ** 2 + c*x + d
elif task_id == 16:
  a = 3
  b = 5
  c = 1
  x = np.linspace(0, 8, 36)
  y = a * (np.sin(b * x) + np.tan(c * x))
elif task_id == 17:
  a = 3
  b = 2
  x = np.linspace(-5, 5, 100)
  y = a * (x**2) * np.cos(b*x)
elif task_id == 18:
  a=2
  b=2
  c=2
  x = np.linspace(0, 10, 100)
  y = a * np.cos(b * x + c)
elif task_id == 19: 
  a = -2
  b = -3
  c = 2
  d = 3
  x = np.linspace(0, 10, 100)
  y = a*np.sin(b*x) + c*np.cos(d*x)
elif task_id == 20:
  a = 5
  b = 10
  c = 3
  x = np.linspace(0,10,100)
  y = a * np.cos(b*x)/x + c
elif task_id == 21: 
  a = 1
  b = 3
  c = 5
  d = 46
  x = np.linspace(-200,200, 200)
  y = a * x ** 4 + b * x ** 3 + c * x + d
elif task_id == 22:
  a = 2
  b = 3
  c = -5
  x = np.linspace(0, 10, 200)
  y = a * x ** -(b * x ** 2 + c)
elif task_id == 23: 
  a = 2
  b = 3
  c = -2
  x = np.linspace(0, 10, 100)
  y = np.log(b*np.sin(c*x))/np.log(a)
elif task_id == 24: 
  a = 2
  b = 2
  c = 20
  d = 2
  x = np.linspace(0.1, 10, 100)
  y = a * np.log((b * x ** 2) / (c * x + d))
elif task_id == 25:
  a = 0.01
  b = 1
  c = 4
  x = np.linspace(-1 * np.pi, 1.5 * np.pi, 1000)
  y = np.cos((a * x ** 2 + b * x + c)) / np.sin((a * x ** 2 + b * x + c))


filename_="Image_"+str(task_id)+".png"
  ############################################################################################################################################
@pytest.mark.mpl_image_compare(baseline_dir='baseline',filename=filename_,tolerance=1)
def test_succeeds():
    color_=color_mas[Var_mas[task_id-1][0]]
    linewidth_=Var_mas[task_id-1][1]
    linestyle_=linestyle_mas[Var_mas[task_id-1][2]]
    plt.plot(x, y, color=color_,linewidth=linewidth_,linestyle=linestyle_)
    return plt.gca().get_figure()
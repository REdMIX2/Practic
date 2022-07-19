#ФАЙЛ DB_P.py ДОЛЖЕН ОТСУТСТВОВАТЬ В КАТАЛОГЕ!!!!
#ЗАПУСКАТЬ СКРИПТ КОМАНДОЙ "python OS_Python_Latex.py" 
import matplotlib.pyplot as plt
import pytest
from matplotlib_assignment import task_id

import sys,subprocess,os
from sys import platform
decode_text=""
if platform == "linux" or platform == "linux2" or platform == "darwin":# linux or win32
    decode_text="utf-8"
elif platform == "win32":
    decode_text="1251"

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
  for i in [25]:#range(1,25+1):
    with open('DB_P.py','w',encoding=decode_text) as f:
      f.write("task_id="+str(i)+"\n")
      f.close()
    c=subprocess.run("pytest --mpl-generate-path=baseline OS_Python_Latex.py", shell=True,capture_output=True)
    tmp =c.stdout.decode(decode_text)
    print(tmp)

if task_id==25:# удаление файла
  os.remove('DB_P.py') 
Var_tex=[r'$y=ax^5+bx^2+cx+d$',              r'$y=a\sin(bx+c)$',            r'$y=\tan(ax^2+bx+c)$',                r'$y=a\ln(b+cx)$',               r'$y=a\ln\frac{x}{b+cx}$',
         r'$y = log_{d}(ax^2+bx+c)$',        r'$y = d^{ax^2+bx+c}$',        r'$y = log_{a}{log_{b}{(cx+d)}}$',     r'$y=\frac{1}{a \ln{|bx+c|}}$',  r'$y=a\sin{bx}+c\sin{dx}$',
         r'$y=ax^2\sin{bx}$',                r'$y=a\frac{\sin(bx)}{x}+c$',  r'$y= \sqrt{\frac{c^2-ax^2}{b}}$',     r'$\begin{cases} y = \sqrt{1-(|x|-1)^{2}} \\ y = arccos(1-|x|)-\pi  \end{cases}$', r'$y=ax^3+bx^2+cx+d$',
         r'$y=a(\sin{bx}+\tan{cx})$',        r'$y=ax^2\cos{bx}$',           r'$y=a\cos(bx+c)$',                    r'$y=a\sin{bx}+c\cos{dx}$',      r'$y=\frac{a\cos{bx}}{x}+c$',
         r'$y=ax^4+bx^3+cx+d$',              r'$y=ax^{-(bx^2+c)}$',         r'$y=log_a(b\sin{cx})$',               r'$y=a\ln{\frac{bx^2}{cx+d}}$',  r'$y=\cot(ax^2+bx+c)}$']
tex=Var_tex[task_id-1]
if task_id==14: 
  tex="".join(tex.split())#delete space in string
  p_b=tex.find(r"\begin{cases}")#delete "\begin{cases}"
  if p_b != -1:
    tex=tex[:p_b]+tex[p_b+13:]
    #print(tex)
  else:
    raise NameError('Incorrect Latex formula')
  p_e=tex.find(r"\end{cases}")
  if p_e != -1:
    tex=tex[:p_e]+tex[p_e+11:]#delete "\end{cases}"
    #print(tex)
  else:
    raise NameError('Incorrect Latex formula')  
  p_slash=tex.find("\\")
  p_slash=tex.find("\\",p_slash+1)
  #print(p_slash)
  if p_slash != -1:
    tex=tex[:p_slash]+tex[p_slash+2:]
    #print(tex)
  else:
    raise NameError('Incorrect Latex formula')

name_latex_file="Latex_"+str(task_id)+".png"
@pytest.mark.mpl_image_compare(baseline_dir='formula_Latex',
                               filename=name_latex_file,tolerance=3)
def test_succeeds():  
  ### Создание области отрисовки
  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  ax.set_axis_off()
  ### Отрисовка формулы
  t = ax.text(0.5, 0.5,tex,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=20, color='black')
  print(tex)      
  ### Определение размеров формулы
  ax.figure.canvas.draw()
  bbox = t.get_window_extent()

  # Установка размеров области отрисовки
  fig.set_size_inches(bbox.width/80,bbox.height/80) # dpi=80

  ### Отрисовка или сохранение формулы в файл
  #plt.show()
  return fig

test_succeeds()
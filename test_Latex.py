import matplotlib.pyplot as plt
import pytest
from matplotlib_assignment import task_id
####### 
#Parsing Latex formulas
import json
from pprint import pprint
with open('matplotlib_assignment.ipynb', 'r') as content_file:
   content = content_file.read()

data=json.loads(content)
tex=""
t=0
for i in data["cells"]:
   if i["source"][0].find("$$")!= -1:
       tex=i["source"][0]
       t=i["source"][0].find("$$")
       break
tex=tex[t+1:tex.find("$$",t+1)+1]#delete $$
#print(tex)
########


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

  #return fig
  ### Отрисовка или сохранение формулы в файл
  plt.show()
  #plt.savefig('test.svg')
  plt.savefig('test.png', dpi=300)
  return fig

test_succeeds()

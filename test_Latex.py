import matplotlib.pyplot as plt
import pytest
####### 
#Парсинг Latex-формулы
import json
from pprint import pprint
with open('matplotlib_assignment.ipynb', 'r') as content_file:
    content = content_file.read()

data=json.loads(content)
tex=''
for i in data["cells"]:
    if i["source"][0].find("$$ y =")!= -1 or i["source"][0].find("$$ y=")!= -1 or i["source"][0].find("$$y =")!= -1 or i["source"][0].find("$$y=")!= -1:
        tex=i["source"][0]
        print(tex)
        break
tex = tex[1:-1]  
print(tex)
########
from matplotlib_assignment import task_id
name_latex_file="Latex_"+str(task_id)+".png"
#tex = '$\\frac{1}{\\sqrt{2\\sqrt{2\\pi}}} \\exp\\left(-\\frac{(x-\\mu)^2}{2\\sigma^2}\\right)$'
@pytest.mark.mpl_image_compare(baseline_dir='formula_Latex',
                               filename=name_latex_file,tolerance=3)
def test_succeeds():  
  ### Создание области отрисовки
  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  ax.set_axis_off()

  ### Отрисовка формулы
  t = ax.text(0.5, 0.5, tex,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=20, color='black')
        
  ### Определение размеров формулы
  ax.figure.canvas.draw()
  bbox = t.get_window_extent()

  # Установка размеров области отрисовки
  fig.set_size_inches(bbox.width/80,bbox.height/80) # dpi=80

  return fig

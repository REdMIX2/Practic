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
#tex = '$\\frac{1}{\\sqrt{2\\sqrt{2\\pi}}} \\exp\\left(-\\frac{(x-\\mu)^2}{2\\sigma^2}\\right)$'
@pytest.mark.mpl_image_compare(baseline_dir='baseline',
                               filename='other_name1.png',tolerance=3)
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
  #print( bbox,width, bbox.height)

  # Установка размеров области отрисовки
  fig.set_size_inches(bbox.width/80,bbox.height/80) # dpi=80
  
  ### Отрисовка или сохранение формулы в файл
 # plt.show()
  #plt.savefig('test.svg')
  #plt.savefig('test.png', dpi=300)
  return fig

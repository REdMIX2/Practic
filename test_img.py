import numpy as np
from matplotlib import pyplot as plt
import pytest
from jupyter_tests import CNT_argv
from matplotlib_assignment import my_function,my_plot,task_id

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
elif task_id == 2:
  a = 2
  b = 2
  c = 3
  x = np.linspace(0, 10, 100)
elif task_id == 3:
  a = 2
  b = 2
  c = 2
  x = np.linspace(0, 10, 100)
elif task_id == 4:
  a = 12
  b = 2
  c = 8
  x = np.linspace(0, 10, 100)
elif task_id == 5:
  a = 5
  b = 100000
  c = 2
  x = np.linspace(0, 10, 25)  
elif task_id == 6:
  a = 100000
  b = 10000
  c = 2
  d = 8
  x = np.linspace(-100, 100, 100)
elif task_id == 7:
  a = 0.5
  b = 1
  c = -3
  d = 0.5
  x = np.linspace(-8, 6, 100)
elif task_id == 8:
  a = 2
  b = 3
  c = 5
  d = 6
  x = np.linspace(0, 100, 1000)
elif task_id == 9:
  a = 1.5
  b = 2
  c = -5
  x = np.linspace(0, 10, 100)
elif task_id == 10:
  a = 3
  b = 4
  c = 2
  d = 7
  x = np.linspace(0, 2*np.math.pi, 100)
elif task_id == 11:
  a = 6
  b = 2
  x = np.linspace(0, 100, 1000)
elif task_id == 12:
  a = 5
  b = 3
  c = -1
  x = np.linspace(1, 20, 200)
if task_id == 13:
  a=1
  b=2
  c=3
  x = np.arange(0, 2*np.math.pi, 0.1)
elif task_id == 14:
  x = np.linspace(-2.1,2.1, 1000)
elif task_id == 15:
  a = 2
  b = 3
  c = -2
  d = 2
  x = np.linspace(-10, 10, 100)
elif task_id == 16:
  a = 3
  b = 5
  c = 1
  x = np.linspace(0, 8, 36)
elif task_id == 17:
  a = 3
  b = 2
  x = np.linspace(-5, 5, 100)
elif task_id == 18:
  a=2
  b=2
  c=2
  x = np.arange(0, 10, 100)
elif task_id == 19: 
  a = -2
  b = -3
  c = 2
  d = 3
  x = np.linspace(0, 10, 100)
elif task_id == 20:
  a = 5
  b = 10
  c = 3
  x = np.linspace(0,10,100)
elif task_id == 21: 
  a = 1
  b = 3
  c = 5
  d = 46
  x = np.linspace(-200,200, 200)
elif task_id == 22:
  a = 2
  b = 3
  c = -5
  x = np.linspace(0, 10, 200)
elif task_id == 23: 
  a = 2
  b = 3
  c = -2
  x = np.linspace(0, 10, 100)
elif task_id == 24: 
  a = 2
  b = 2
  c = 20
  d = 2
  x = np.linspace(0.1, 10, 100)
elif task_id == 25:
  a = 0.01
  b = 1
  c = 4
  x = np.linspace(-1 * np.pi, 1.5 * np.pi, 1000)
  ############################################################################################################################################
  
if CNT_argv[task_id-1] == 0:
  y=my_function(x)
elif CNT_argv[task_id-1] == 1:
  y=my_function(x,a)
elif CNT_argv[task_id-1] == 2:
  y=my_function(x,a,b)
elif CNT_argv[task_id-1] == 3:
  y=my_function(x,a,b,c)
elif CNT_argv[task_id-1] == 4:
  y=my_function(x,a,b,c,d)
name_img_file="Image_"+str(task_id)+".png"
@pytest.mark.mpl_image_compare(baseline_dir='images_of_graphs',
                               filename=name_img_file,tolerance=100)
def test_succeeds():
  my_plot()
  return plt.gca().get_figure()

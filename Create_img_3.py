import numpy as np
from matplotlib import pyplot as plt
import pytest
from jupyter_tests import CNT_argv
from matplotlib_assignment import my_function,my_plot,task_id

a=0
b=0
c=0
d=0
x = np.arange(0, 2*np.math.pi, 0.1)
y=[]
if task_id == 13:
  a=1
  b=2
  c=3
  d=2
  x = np.arange(0, 2*np.math.pi, 0.1)
elif task_id == 5:
  a = 5
  b = 100000
  c = 2
  x = np.linspace(0, 10, 25)  
elif task_id == 7:
  b = 1
  c = 1
  d = 2
  x = np.linspace(0, 0.5, 20)
elif task_id == 18:
  a=2
  b=2
  c=2
  d=2
  x = np.arange(0, 10, 100)
elif task_id == 16:
  a = 3
  b = 5
  c = 1
  x = np.linspace(0, 8, 36)
elif task_id == 25:
  a = 0.01
  b = 1
  c = 4
  x = np.linspace(-1 * np.pi, 1.5 * np.pi, 1000)
elif task_id == 9:
  a = 1.5
  b = 2
  c = -5
  x = np.linspace(0, 10, 100)
elif task_id == 2:
  a = 12
  b = 2
  c = 8
  x = np.linspace(0, 10, 100)
if CNT_argv[task_id] == 0:
  y=my_function(x)
elif CNT_argv[task_id] == 1:
  y=my_function(x,a)
elif CNT_argv[task_id] == 2:
  y=my_function(x,a,b)
elif CNT_argv[task_id] == 3:
  y=my_function(x,a,b,c)
elif CNT_argv[task_id] == 4:
  y=my_function(x,a,b,c,d)

@pytest.mark.mpl_image_compare(filename='other_name1.png',tolerance=3)
def test_succeeds():
  my_plot()
  return plt.gca().get_figure()

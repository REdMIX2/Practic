import numpy as np
from matplotlib import pyplot as plt
import pytest
from jupyter_tests import CNT_argv
from matplotlib_assignment import my_function,my_plot,task_id
a=1
b=2
c=3
d=2
x = np.arange(0, 2*np.math.pi, 0.1)
y=[]
match CNT_argv[task_id]:
  case 1:
    global y
    y=my_function(x)
  case 2:
    global y
    y=my_function(x,a)
  case 3:
    global y
    y=my_function(x,a,b)
  case 4:
    global y
    y=my_function(x,a,b,c,d)
@pytest.mark.mpl_image_compare(filename='other_name1.png',tolerance=3)
def test_succeeds():
  my_plot()
  return plt.gca().get_figure()

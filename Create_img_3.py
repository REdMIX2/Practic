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

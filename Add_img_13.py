import numpy as np
from matplotlib import pyplot as plt
import pytest
a=1
b=2
c=3
x = np.arange(0, 20, 0.1)
from matplotlib_assignment import my_plot
def my_function(x, a, b, c):
  ### BEGIN YOUR CODE
  import numpy as np
  return np.sqrt((np.square(c) - a * x **2)/ b)+100
y=my_function(x,a,b,c)
@pytest.mark.mpl_image_compare(filename='other_name1.png',tolerance=3)
def test_succeeds():
  my_plot()
  return plt.gca().get_figure()

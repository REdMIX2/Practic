import numpy as np
from matplotlib import pyplot as plt
import pytest
a=1
b=2
c=3
x = np.arange(0, 2*np.math.pi, 0.1)
from matplotlib_assignment import my_plot
def my_function(x, a, b, c):
  ### BEGIN YOUR CODE
  import numpy as np
  return a+b+c+x
y=my_function(x,a,b,c)
@pytest.mark.mpl_image_compare(filename='other_name1.png',tolerance=3)
def test_succeeds():
  #plt.plot(x, y, color='purple', marker='o', linewidth=1, markersize=10)
  my_plot()
  return plt.gca().get_figure()

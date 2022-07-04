import numpy as np
from matplotlib import pyplot as plt
import pytest
from matplotlib_assignment import my_function,my_plot

@pytest.mark.mpl_image_compare(baseline_dir='baseline',
                               filename='other_name1.png',tolerance=3)
def test_succeeds():
  a=2
  b=2
  c=2
  d=2
  x = np.arange(0, 2*np.math.pi, 0.1)
  y=my_function(x,a,b,c)
  my_plot()
 return plt.gca().get_figure()

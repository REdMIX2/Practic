jupyter_tests.py
Скрипт с тестами, которые тестируют файлы jupyter_assignment.py  и matplotlib_assignment.py

test_img.py
	Скрипт тестирует изображение графика, сравнивая  сгенерированное изображение( с помощью пользовательских  функций my_function и my_plot)
  c базовым(эталонным изображением в папке images_of_graphs)

test_Latex.py
	Скрипт парсит latex-формулу из matplotlib_assignment.ipynb, а после тестирует изображение latex-формулы, сравнивая  сгенерированное
  изображение( с помощью поддержки библиотекой matplotlib вывода latex-формулы) c базовым(эталонным изображением в папке formula_Latex)

OS_Python_Create_IMG.py(для преподавателя)
	Скрипт для генерации всех 25 изображений графиков с их индивидуальными параметрами линии.Рекурсивный(т.е. запускает свой же файл для каждого графика).
  Запускается командой “python OS_Python_Create_IMG.py” ,
  работает около 1 минуты.
OS_Python_Latex.py(для преподавателя)
	Скрипт для генерации всех 25 графиков с Latex-формулами.Рекурсивный(т.е. запускает свой же файл для каждой формулы).
  Запускается командой  “python OS_Python_Latex.py”, работает около 1 минуты.

from distutils.core import setup
from Cython.Build import cythonize

# setup(ext_modules = cythonize('bivariate.pyx'))
setup(ext_modules = cythonize('trivariate.pyx'))
from os import path
from setuptools import setup

setup(name='gym_x',
      version='0.0.2',
      url='https://github.com/koulanurag/gym_x',
      py_modules=['gym_x'],
      packages=['gym_x'],
      author='Anurag Koul',
      author_email='koulanurag@gmail.com',
      long_description=open(path.join(path.abspath(path.dirname(__file__)), 'README.md')).read(),
      license='MIT',
      install_requires=['gym==0.12'],
      )

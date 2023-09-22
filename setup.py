from setuptools import setup, find_packages

setup(name='rfdiffusion',
      version='1.1.0',
      description='RFdiffusion is an open source method for protein structure generation.',
      author='Rosetta Commons',
      url='https://github.com/RosettaCommons/RFdiffusion',
      entry_points=dict(console_scripts=['rfdiffusion = rfdiffusion.inference:main']),
      packages=find_packages(),
      install_requires=['torch', 'se3-transformer'])

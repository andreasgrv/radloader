from setuptools import setup, find_packages

setup(
      name='radloader',
      packages=find_packages(include=['radloader', 'radloader.*']),
      version='0.0.1',
      author='Andreas Grivas',
      author_email='agrivas@ed.ac.uk',
      description='radloader',
      license='BSD',
      keywords=['Radiology reports'],
      scripts=[],
      classifiers=[],
      # We are depending on dict order insertion (new in 3.7)
      # + we are using dataclasses
      python_requires='>=3.7',
      tests_require=['pytest']
)

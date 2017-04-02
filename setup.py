from setuptools import setup
import io

with io.open('README.rst', encoding="utf-8") as f:
    long_description = f.read()


setup(name='pycdiscount',
      version='0.3.5',
      description='A simple Python Wrapper for CDiscount API using Requests.',
      long_description=long_description,
      url='https://github.com/wblondel/PythonCdiscountWrapper',
      author='William Gerald Blondel',
      author_email='contact@williamblondel.fr',
      install_requires=["requests"],
      include_package_data=True,
      license='GNU GPL',
      packages=['pycdiscount'],
      classifiers=[
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Topic :: Internet",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
      ],
      zip_safe=False)

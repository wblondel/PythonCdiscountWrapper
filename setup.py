from setuptools import setup

setup(name='pycdiscount',
      version='0.3.2',
      description='A simple Python Wrapper for CDiscount API using Requests.',
      url='https://github.com/wblondel/PythonCdiscountWrapper',
      author='William Gerald Blondel',
      author_email='contact@williamblondel.me',
      install_requires=["requests"],
      include_package_data=True,
      license='GNU GPL',
      packages=['pycdiscount'],
      classifiers=[
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Programming Language :: Python :: 3.4",
          "Topic :: Internet",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
      ],
      zip_safe=False)

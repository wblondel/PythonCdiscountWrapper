PythonCdiscount
===============

PythonCdiscount is a small wrapper around the `Cdiscount <https://cdiscount.com>`__ `Products
API <https://dev.cdiscount.com/home>`__.

Requirements
------------

PythonCdiscount requires Requests, an elegant and simple HTTP library for Python, built for human
beings.

    http://docs.python-requests.org/

You also need a Cdiscount API key, which you can get from here : https://dev.cdiscount.com

Installation
------------

::

    pip install pycdiscount

Example Use
-----------

.. code:: python

    from pycdiscount import PyCdiscount
    app = PyCdiscount(api_key="YOUR API KEY")
    searchresult = app.search("Iphone")

All results are returned in JSON format. If you want to show them in the console, I suggest you use
the pprint module.

    https://docs.python.org/3/library/pprint.html

Questions, Comments, etc?
-------------------------

Feel free to hit me up at the following:

| GitHub: https://github.com/wblondel
| Twitter: http://twitter.com/wgblondel
| Email: contact@williamblondel.fr

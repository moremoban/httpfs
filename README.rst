================================================================================
httpfs
================================================================================

.. image:: https://api.travis-ci.org/moremoban/httpfs.svg
   :target: http://travis-ci.org/moremoban/httpfs

.. image:: https://codecov.io/github/moremoban/httpfs/coverage.png
   :target: https://codecov.io/github/moremoban/httpfs
.. image:: https://img.shields.io/github/stars/moremoban/httpfs.svg?style=social&maxAge=3600&label=Star
    :target: https://github.com/moremoban/httpfs/stargazers

.. image:: https://dev.azure.com/moremoban/httpfs/_apis/build/status/moremoban.httpfs?branchName=master
   :target: https://dev.azure.com/moremoban/httpfs/_build/latest?definitionId=2&branchName=master


It enables moban to use any files over http(s) as its template or data file:

.. code-block:: bash

    $ moban -t 'https://raw.githubusercontent.com/moremoban/pypi-mobans/dev/templates/_version.py.jj2'\
      -c 'https://raw.githubusercontent.com/moremoban/pypi-mobans/dev/config/data.yml'\
      -o _version.py


Installation
================================================================================

You can get it:

.. code-block:: bash

    $ git clone https://github.com/moremoban/httpfs.git
    $ cd httpfs
    $ python setup.py install

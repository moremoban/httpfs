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


Capability contraints
================================================================================

Only one http url can be used with `template_dir` inside a mobanfile. Simply
HTTP interface do not allow directory list. Hence, no way to tell if a file
falls in one url but not another.

In an edge case, if github repo's public url is given for a moban project,
this github repo shall not have sub repos. This library will fail to
translate sub-repo as url.


Installation
================================================================================

You can get it:

.. code-block:: bash

    $ git clone https://github.com/moremoban/httpfs.git
    $ cd httpfs
    $ python setup.py install

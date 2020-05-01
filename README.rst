================================================================================
httpfs
================================================================================

.. image:: https://api.travis-ci.org/moremoban/httpfs.svg
   :target: http://travis-ci.org/moremoban/httpfs

.. image:: https://codecov.io/github/moremoban/httpfs/coverage.png
   :target: https://codecov.io/github/moremoban/httpfs
.. image:: https://img.shields.io/github/stars/moremoban/httpfs.svg?style=social&maxAge=3600&label=Star
    :target: https://github.com/moremoban/httpfs/stargazers


What can you do with it?
================================================================================

.. code::

   >>> import fs
   >>> with fs.open_fs('https://www.google.com') as f:
   ...     print(f.readbytes('index.html'))
   b'<!doctype ....'

Have fun!

Why
================================================================================

Its creation was to enable `moban`_ to use any files over http(s) as its
template or data file:

.. code-block:: bash

    $ moban -t 'https://raw.githubusercontent.com/moremoban/pypi-mobans/dev/templates/_version.py.jj2'\
      -c 'https://raw.githubusercontent.com/moremoban/pypi-mobans/dev/config/data.yml'\
      -o _version.py


.. _moban: https://github.com/moremoban/moban

Capability contraints
================================================================================

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

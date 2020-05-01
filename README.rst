================================================================================
httpfs
================================================================================

.. image:: https://api.travis-ci.org/moremoban/httpfs.svg
   :target: http://travis-ci.org/moremoban/httpfs

.. image:: https://codecov.io/github/moremoban/httpfs/coverage.png
   :target: https://codecov.io/github/moremoban/httpfs
.. image:: https://badge.fury.io/py/httpfs.svg
   :target: https://pypi.org/project/httpfs

.. image:: https://pepy.tech/badge/httpfs/month
   :target: https://pepy.tech/project/httpfs/month

.. image:: https://img.shields.io/github/stars/moremoban/httpfs.svg?style=social&maxAge=3600&label=Star
    :target: https://github.com/moremoban/httpfs/stargazers


What can you do with it?
================================================================================

With `Python File System 2`_, you can do:

.. code::

   >>> import fs
   >>> with fs.open_fs('https://www.google.com') as f:
   ...     print(f.readbytes('index.html'))
   b'<!doctype ....'

Have fun!

Why
================================================================================

It enables `moban`_ to use any files over http(s) as its
template or data file:

.. code-block:: bash

    $ moban -t 'https://raw.githubusercontent.com/moremoban/pypi-mobans/dev/templates/_version.py.jj2'\
      -c 'https://raw.githubusercontent.com/moremoban/pypi-mobans/dev/config/data.yml'\
      -o _version.py


.. _Python File System 2: https://docs.pyfilesystem.org/en/latest
.. _moban: https://github.com/moremoban/moban


Installation
================================================================================


You can install httpfs via pip:

.. code-block:: bash

    $ pip install httpfs


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/moremoban/httpfs.git
    $ cd httpfs
    $ python setup.py install

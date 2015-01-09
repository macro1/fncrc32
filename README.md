FileName CRC32
==============

A tool to check file hashes against gzip compatible CRC32 hash values
in filenames.


Usage
-----

    $ fncrc32 \[Commie\]\ *
      [ d533e298 ] "[Commie] Guilty Crown - 00 Lost Christmas [D533E298].mkv"
      [ 662bb1fd ] "[Commie] Guilty Crown - 01 [662BB1FD].mkv"


Install requirements
--------------------

    $ pip install -r requirements.txt


Run tests
---------

Run tests in all available environments with `tox`

    $ tox

Or run `cram` in the current environment

    $ cram -E tests/

The flag is necessary to preserve the terminal encoding environment variables.

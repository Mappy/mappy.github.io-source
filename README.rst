Mappy Tech Blog
===============

.. image:: https://secure.travis-ci.org/Mappy/mappy.github.io-source.png
   :target: http://travis-ci.org/Mappy/mappy.github.io-source

About
-----

That project (mappy.github.io-source) hosts source code and content for the `Mappy technical blog <http://techblog.mappy.com/>`_.

The blog content is written in Markdown and is built using Pelican.

We’re using `Travis <https://travis-ci.org/>`_ to build and publish the blog into a separate project (mappy.github.io), served via Github Pages.

How to build locally
--------------------

Install dependencies via ``pip install -r requirements.txt`` or ``apt-get install python-pelican fabric``.

Use `make html` to transform Markdown to HTML then `make html` to launch a local webserver.

You can see your work at http://localhost:8000.

How to publish
--------------

Simply push your(s) commit(s).

Travis will then build and publish your work.

References
----------

- http://zonca.github.io/2013/09/automatically-build-pelican-and-publish-to-github-pages.html


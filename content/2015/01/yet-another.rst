########################################################################
Almost Ready!
########################################################################

:date: 2014-12-20 13:00
:tags:
:category:
:slug: sample-first-blog
:author: Don Parakin
:summary: Almost ready. Currently configuring and customizing the blog
    static site generator, `Pelican <http://www.getpelican.com/>`_.

    This blog is a sample of what can be done with Pelican and ReST.
    Read more to see the samples ... and the styling (now in progress).

COMING SOON! Really! What you see here is the UNDER CONSTRUCTION.
Just need to finish the styling and configuring and I'll be ready to go.

One of the nice things about ReST and Pelican is that it will generate
a table of contents automagically.  This was genereated with one line of markup.

.. contents::

************************************************************************
Demo of ReST
************************************************************************

Okay, the rest of this page is for demoing ReST ... so that I my
style the elements as required.

You can also add pop-ups for an abbreviation: try :abbr:`DP (Don Parakin)`
(hover over the "DP").

Also nice is that ReST will do footnotes [#fn1]_.  Ensure that a space is encoded
before the reference [#fn2]_ in the markup.

ReST can also do a `cross-link <{filename}blog-3.rst>`_ to another page
within this same web site (an "internal" reference).

Of course, can do some code with highlighting by pygments ...

.. code-block:: python
    :linenos: table
        :linenostart: 153

       def myfunc1():
           pass
       def myfunc2():
           pass

************************************************************************
Heading 2
************************************************************************

Here's some more text.  This is a breaking paragraph with a link to `Toronto HOG`_ before I try something new.

::

    Not quite sure what this does but it is called a "literal block". An empty line is required between
    the double colons and the literal block's text (indented too).



.. note:: Here's a note that I've added to the markup. Still have to do the styling of this (until
    then it won't look like much).

This next thing is really cool: math equations!

.. math::

    n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

.. sidebar:: By The Way

    Here's some text that's in my "side bar". Here's some text that's in my "side bar". Here's some text that's in my "side bar".
    Here's some text that's in my "side bar". Here's some text that's in my "side bar".

Not such a good idea to finish with a side bar. It appears to belong to the next heading.

========================================================================
Heading 3
========================================================================

And to be able to use |alias| and have it expanded for me.

Here's some text under this heading.Here's some text under this heading.Here's some text under this heading.
Here's some text under this heading. Here's some text under this heading.

Here's some text under this heading. Here's some text under this heading. Here's some text under this heading.
Here's some text under this heading.

------------------------------------------------------------------------
Heading 4 is More
------------------------------------------------------------------------

Here's some text under this heading. Here's some text under this heading. Here's some text under this heading.
Here's some text under this heading. Here's some text under this heading. Here's some text under this heading.

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
Heading 5 is More
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

Here's some text under this heading. Here's some text under this heading. Here's some text under this heading.

........................................................................
Heading 6 is More
........................................................................

Here's some text under this heading. Here's some text under this heading. Here's some text under this heading.
Here's some text under this heading. Here's some text under this heading. Here's some text under this heading.


.. _Toronto HOG: http://www.torontohog.com/

.. [#fn1] Might just be a footnote for the word abbreviation above.

.. [#fn2] And here is the text of a 2nd footnote. Wow!

.. |alias| replace:: (this was an "alias"; replaced by this text)
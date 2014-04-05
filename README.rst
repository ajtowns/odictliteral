from odictliteral import odict
==============================

Provides a nice way of specifying ordered dictionaries from Python source.

Example:

    >>> from odictliteral import odict
    >>> x = odict[1:2,3:4]
    >>> print(x)
    odict[1: 2, 3: 4]

You can use odict as a replacement for OrderedDict otherwise, eg:

    >>> y = odict( [(1,2), (3,4)] )
    >>> print(y)
    odict[1: 2, 3: 4]
    >>> x == y
    True

You should also be able to use odict in combination with OrderedDicts:

    >>> z = OrderedDict( [(1,2), (3,4)] )
    >>> print(z)
    OrderedDict([(1, 2), (3, 4)])
    >>> y == z
    True

That's pretty much all there is to it. Should be compatible with Python
2.7 and Python 3; requires the "ordereddict" module to work with Python
2.4, 2.5 or 2.6.


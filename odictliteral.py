try:
    from collections import OrderedDict
except:
    from ordereddict import OrderedDict

try:
    from reprlib import recursive_repr
except:
    # don't cope with recursive repr calls in py2
    def recursive_repr(fillvalue='...'): return (lambda f: f)

try:
    from collections.abc import Iterable
except:
    Iterable = tuple

__all__ = ["odict"]
__version__ = '1.0.0'

class odictType(type):
    syntax_error = SyntaxError("Allowed syntax: odict[<k>: <v>(, <k>: <v>...)]")

    def __getitem__(self, keys):
        if isinstance(keys, slice):
            keys = (keys,)
        if not isinstance(keys, Iterable):
            raise self.syntax_error
        od = self()
        for k in keys:
            if not isinstance(k, slice) or k.step is not None:
                raise self.syntax_error
            od[k.start] = k.stop
        return od

@recursive_repr(fillvalue="odict[...]")
def odict_repr(self):
    if len(self) == 0:
        return "odict()"
    else:
        return "odict[%s]" % (", ".join("%s: %s" % (k,v) for k,v in self.items()),)

odict = odictType(str('odict'), (OrderedDict,), {"__repr__": odict_repr})

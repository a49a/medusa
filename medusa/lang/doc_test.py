class Dict(dict):
    """
    >>> d1 = Dict()
    >>> d1['x'] = 1
    >>> d1.x
    1

    """

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"{key}")

    def __setattr__(self, key, value):
        self[key] = value


if "__main__" == __name__:
    import doctest
    doctest.testmod()

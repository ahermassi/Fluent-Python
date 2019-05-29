class StrKeyDict(dict):

    def __missing__(self, key):  # __missing__ is only called when a non existing key is accessed with d[key]

        if isinstance(key, str):
            raise KeyError
        return self[str(key)]

    def get(self, key, default=None):

        try:
            return self[key]  # self[key] delegates to __getitem__ which calls __missing__ if key is missing
        except KeyError:
            return default

    def __contains__(self, key): # __contains__ and so "in" don't delegate to __missing__
        return key in self.keys() or str(key) in self.keys()


if __name__ == '__main__':

    d = StrKeyDict([('1', 'one'), ('2', 'two')])

    print(d['1'])
    print(d[2])
    # print(d[3])

    print(d.get('1'))
    print(d.get(2))
    print(d.get(3, 'N/A'))

    print(2 in d)
    print(3 in d)

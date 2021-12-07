from collections import OrderedDict


class LruDict(OrderedDict):

    def __init__(self, cap: int = 128, *args, **kwargs):
        super(LruDict, self).__init__(*args, **kwargs)
        self.cap: int = cap

    def __getitem__(self, item):
        result = super(LruDict, self).__getitem__(item)
        if result:
            self.move_to_end(item)
        return result

    def __setitem__(self, key, value):
        if key in self:
            super(LruDict, self).__setitem__(key, value)
            self.move_to_end(key)
        else:
            super(LruDict, self).__setitem__(key, value)
            if len(self) > self.cap:
                old_key = next(iter(self))
                self.__delitem__(old_key)


def test_lru():
    lr = LruDict(5)
    lr["a"] = 1
    lr["b"] = 2
    lr["c"] = 3
    lr["d"] = 4
    lr["e"] = 5
    print(lr)
    print("b:", lr["b"])
    print(lr)
    lr["a"] = "x"
    print(lr)
    print("c:", lr["c"])
    print(lr)
    lr["f"] = 6
    print(lr)


test_lru()

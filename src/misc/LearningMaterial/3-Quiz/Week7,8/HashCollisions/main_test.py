from stencil import *


def test_hashmap_basic():
    h = Hashmap(10)
    h.insert(1, "first")
    h.insert(11, "second")
    h.insert(21, "third")
    h.insert(31, "fourth")
    h.insert(41, "fifth")

    # Test that the insert method correctly assigns values to keys
    assert h.get(1) == "first"
    assert h.get(11) == "second"
    assert h.get(21) == "third"
    assert h.get(31) == "fourth"
    assert h.get(41) == "fifth"
    assert h.get(55) is None
    assert h.get(2) is None
    assert h.get(4) is None

    # test that the items method returns a list of tuples in the form (key,val)
    assert set(h.items()) == {(1, "first"), (11, "second"), (21, "third"), (31, "fourth"), (41, "fifth")}

    # test that collision handling works correctly
    h.insert(1, "updated_first")
    assert h.get(1) == "updated_first"
    assert set(h.items()) == {(1, "updated_first"), (11, "second"), (21, "third"), (31, "fourth"), (41, "fifth")}

    def test_larger_collisions():
        h = Hashmap(10)
        keys = [i * 10 + 1 for i in range(10)]  # keys are 1,11,21,31....101
        vals = ["val{}".format(i) for i in range(10)]  # vals are in form of val0, val1, val2, ...
        for i in range(len(keys)):
            h.insert(keys[i], vals[i])

        # test that the first key and value have been properly inserted
        assert h.get(keys[0]) == vals[0]

        # test that the last key and value have been properly inserted
        assert h.get(keys[-1]) == vals[-1]

        # test that all keys and values have been properly inserted
        assert set(h.items()) == {[(keys[i], vals[i]) for i in range(10)]}

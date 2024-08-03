from mergr.merger import Merger


def test_mappings_shallowly_merged():
    merge = Merger()

    assert merge({1: 1}, {2: 2}) == {1: 1, 2: 2}
    assert merge({1: 1, 2: 2}, {2: 3}) == {1: 1, 2: 3}
    assert merge({1: 1, 2: {3: 3}}, {2: 4}) == {1: 1, 2: 4}


def test_does_not_mutate_input_mappings():
    merge = Merger()

    a = {1: 1}
    b = {2: 2}

    assert merge(a, b) == {1: 1, 2: 2}

    assert a == {1: 1}
    assert b == {2: 2}


def test_fallback_to_default_if_b_is_not_mapping():
    merge = Merger()

    assert merge(None, {1: 1}) is None
    assert merge({1: 1}, None) == {1: 1}
    assert merge({1: 1}, 2) == {1: 1}
    assert merge({1: 1}, "2") == {1: 1}
    assert merge({1: 1}, [2]) == {1: 1}

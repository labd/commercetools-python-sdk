from commercetools import types


def test_equality():
    obj_1 = types.ProductDraft(slug="test-1")
    obj_2 = types.ProductDraft(slug="test-2")

    assert obj_1 != obj_2

    obj_1 = types.ProductDraft(slug="test-1")
    obj_2 = types.ProductDraft(slug="test-1")
    assert obj_1 == obj_2


def test_gt_lt():
    obj_1 = types.ProductDraft(slug="test-1", name="foo")
    obj_2 = types.ProductDraft(slug="test-1", name="bar")

    assert obj_1 > obj_2
    assert not obj_1 < obj_2

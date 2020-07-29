import pytest
import utils


@pytest.mark.parametrize(
    "test_input,test_output",
    [("fooBar", "foo_bar"), ("externalOAuth", "external_oauth")],
)
def test_snakit(test_input, test_output):
    assert utils.snakeit(test_input) == test_output


def test_format_docstring():
    value = "Returns a customer by its ID from a specific Store. The {storeKey} path parameter maps to a Store's key.\nIt also considers customers that do not have the stores field.\nIf the customer exists in the commercetools project but the stores field references different stores,\nthis method returns a ResourceNotFound error.\n"

    newvalue = utils.format_docstring(value)
    assert (
        newvalue
        == """Returns a customer by its ID from a specific Store.

        The {storeKey} path parameter maps to a Store's key.
        It also considers customers that do not have the stores field.
        If the customer exists in the commercetools project but the stores field references different stores,
        this method returns a ResourceNotFound error.
    """
    )

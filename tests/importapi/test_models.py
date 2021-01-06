import pprint

from commercetools.importapi import models


def test_serialization_optional_values():
    item = models.LineItemImportDraft(
        name={"nl-NL": "foobar"},
        variant=models.LineItemProductVariantImportDraft(sku="foobar"),
        price=models.LineItemPrice(
            value=models.Money(cent_amount=1000, currency_code="EUR"),
        ),
        quantity=3,
    )

    data = item.serialize()
    item_cycle = models.LineItemImportDraft.deserialize(data)
    data_cycle = item_cycle.serialize()

    expected = {
        "name": {"nl-NL": "foobar"},
        "price": {
            "value": {
                "centAmount": 1000,
                "currencyCode": "EUR",
                "type": "centPrecision",
            }
        },
        "quantity": 3.0,
        "variant": {"sku": "foobar"},
    }
    assert expected == data
    assert expected == data_cycle

import datetime

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


def test_serialization_optional_values():
    now = datetime.datetime(2021, 1, 30, 11, 21, 8)
    custom = models.Custom(
        type=models.TypeKeyReference(key="my-custom-type"),
        fields=models.FieldContainer(
            {
                "foo": models.NumberField(value=1234),
                "itemDate": models.DateTimeField(value=now),
            }
        ),
    )
    data = custom.serialize()
    expected = {
        "fields": {
            "foo": {
                "type": "Number",
                "value": 1234,
            },
            "itemDate": {
                "type": "DateTime",
                "value": "2021-01-30T11:21:08",
            },
        },
        "type": {"typeId": "type", "key": "my-custom-type"},
    }
    assert data == expected

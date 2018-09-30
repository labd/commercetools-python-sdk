from commercetools import schemas, types


def test_serialize_field_container():

    draft = types.CustomFieldsDraft(
        type=types.ResourceIdentifier(type_id=types.ReferenceTypeId.CART, id="foobar"),
        fields=types.FieldContainer(foobar=10),
    )

    result = schemas.CustomFieldsDraftSchema().dump(draft)
    expected = {
        "fields": {"foobar": 10},
        "type": {"typeId": "cart", "id": "foobar", "key": None},
    }
    assert expected == result

    roundtrip = schemas.CustomFieldsDraftSchema().load(expected)
    assert draft == roundtrip

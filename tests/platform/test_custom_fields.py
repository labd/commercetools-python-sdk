from commercetools.platform import models
from commercetools.platform.models._schemas.type import CustomFieldsDraftSchema


def test_serialize_field_container():

    draft = models.CustomFieldsDraft(
        type=models.TypeResourceIdentifier(id="foobar"),
        fields=models.FieldContainer(foobar=10),
    )

    result = CustomFieldsDraftSchema().dump(draft)
    expected = {
        "fields": {"foobar": 10},
        "type": {"typeId": "type", "id": "foobar", "key": None},
    }
    assert expected == result

    roundtrip = CustomFieldsDraftSchema().load(expected)
    assert draft == roundtrip

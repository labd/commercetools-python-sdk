from commercetools.platform import models
from commercetools.platform.models._schemas.type import CustomFieldsDraftSchema


def test_serialize_field_container():

    draft = models.CustomFieldsDraft(
        type=models.TypeResourceIdentifier(id="foobar"),
        fields=models.FieldContainer(foobar=10),
    )

    result = draft.serialize()
    expected = {
        "fields": {"foobar": 10},
        "type": {"typeId": "type", "id": "foobar"},
    }
    assert expected == result

    roundtrip = models.CustomFieldsDraft.deserialize(expected)
    assert draft == roundtrip

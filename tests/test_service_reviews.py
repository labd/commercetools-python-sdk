from commercetools import schemas, types


def test_get_by_id(client):
    review = client.reviews.create(draft=schemas.ReviewDraftSchema().dump({}))
    assert review.id

    review = client.reviews.get_by_id(review.id)
    assert review


def test_get_by_key(client):
    review = client.reviews.create(
        draft=schemas.ReviewDraftSchema().dump({"key": "test-review"})
    )
    assert review.key

    review = client.reviews.get_by_key(review.key)
    assert review


def test_query(client):
    pass


def test_delete_by_id(client):
    review = client.reviews.create(draft=types.ReviewDraft())
    assert review.id
    assert client.reviews.delete_by_id(review.id, version=review.version)


def test_delete_by_key(client):
    review = client.reviews.create(
        draft=schemas.ReviewDraftSchema().dump({"key": "test-review"})
    )
    assert review.key
    assert client.reviews.delete_by_key(review.key, version=review.version)

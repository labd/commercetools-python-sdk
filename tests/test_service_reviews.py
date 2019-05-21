from commercetools import schemas, types


def test_create_review(client):
    review = client.reviews.create(draft=types.ReviewDraft(rating=3))

    assert review.id
    assert review.rating == 3


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
    client.reviews.create(draft=types.ReviewDraft(key="test-review-1"))
    client.reviews.create(draft=types.ReviewDraft(key="test-review-2"))

    result = client.reviews.query(sort="id asc", limit=10)
    assert len(result.results) == 2
    assert result.total == 2

    result = client.reviews.query(sort=["id asc", "name asc"], limit=1)
    assert len(result.results) == 1
    assert result.total == 2


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

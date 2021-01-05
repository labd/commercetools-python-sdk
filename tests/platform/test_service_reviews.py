from commercetools.platform import models
from commercetools.platform.models._schemas.review import ReviewDraftSchema


def test_create_review(old_client):
    review = old_client.reviews.create(draft=models.ReviewDraft(rating=3))

    assert review.id
    assert review.rating == 3


def test_get_by_id(old_client):
    review = old_client.reviews.create(draft=models.ReviewDraft())
    assert review.id

    review = old_client.reviews.get_by_id(review.id)
    assert review


def test_get_by_key(old_client):
    review = old_client.reviews.create(draft=models.ReviewDraft(key="test-review"))
    assert review.key

    review = old_client.reviews.get_by_key(review.key)
    assert review


def test_query(old_client):
    old_client.reviews.create(draft=models.ReviewDraft(key="test-review-1"))
    old_client.reviews.create(draft=models.ReviewDraft(key="test-review-2"))

    result = old_client.reviews.query(sort="id asc", limit=10)
    assert len(result.results) == 2
    assert result.total == 2

    result = old_client.reviews.query(sort=["id asc", "name asc"], limit=1)
    assert len(result.results) == 1
    assert result.total == 2


def test_delete_by_id(old_client):
    review = old_client.reviews.create(draft=models.ReviewDraft())
    assert review.id
    assert old_client.reviews.delete_by_id(review.id, version=review.version)


def test_delete_by_key(old_client):
    review = old_client.reviews.create(draft=models.ReviewDraft(key="test-review"))
    assert review.key
    assert old_client.reviews.delete_by_key(review.key, version=review.version)

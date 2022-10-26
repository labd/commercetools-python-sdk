from commercetools.platform import models
from commercetools.platform.client import Client
from commercetools.platform.models._schemas.review import ReviewDraftSchema


def test_create_review(ct_platform_client: Client):
    review = (
        ct_platform_client.with_project_key("unittest")
        .reviews()
        .post(models.ReviewDraft(rating=3))
    )

    assert review.id
    assert review.rating == 3


def test_with_id_get(ct_platform_client: Client):
    review = (
        ct_platform_client.with_project_key("unittest")
        .reviews()
        .post(models.ReviewDraft())
    )
    assert review.id

    review = (
        ct_platform_client.with_project_key("unittest")
        .reviews()
        .with_id(review.id)
        .get()
    )
    assert review


def test_get_by_key(ct_platform_client: Client):
    review = (
        ct_platform_client.with_project_key("unittest")
        .reviews()
        .post(models.ReviewDraft(key="test-review"))
    )
    assert review.key

    review = (
        ct_platform_client.with_project_key("unittest")
        .reviews()
        .with_key(review.key)
        .get()
    )
    assert review


def test_query(ct_platform_client: Client):
    ct_platform_client.with_project_key("unittest").reviews().post(
        models.ReviewDraft(key="test-review-1")
    )
    ct_platform_client.with_project_key("unittest").reviews().post(
        models.ReviewDraft(key="test-review-2")
    )

    result = (
        ct_platform_client.with_project_key("unittest")
        .reviews()
        .get(sort="id asc", limit=10)
    )
    assert len(result.results) == 2
    assert result.total == 2

    result = (
        ct_platform_client.with_project_key("unittest")
        .reviews()
        .get(sort=["id asc", "name asc"], limit=1)
    )
    assert len(result.results) == 1
    assert result.total == 2


def test_delete_by_id(ct_platform_client: Client):
    review = (
        ct_platform_client.with_project_key("unittest")
        .reviews()
        .post(models.ReviewDraft())
    )
    assert review.id
    assert (
        ct_platform_client.with_project_key("unittest")
        .reviews()
        .with_id(review.id)
        .delete(version=review.version)
    )


def test_delete_by_key(ct_platform_client: Client):
    review = (
        ct_platform_client.with_project_key("unittest")
        .reviews()
        .post(models.ReviewDraft(key="test-review"))
    )
    assert review.key
    assert (
        ct_platform_client.with_project_key("unittest")
        .reviews()
        .with_key(review.key)
        .delete(version=review.version)
    )

from commercetools.platform import models
from commercetools.platform.client import Client


def test_project_update_countries(ct_platform_client: Client):
    project = ct_platform_client.with_project_key("unittest").get()
    assert project
    project = ct_platform_client.with_project_key("unittest").post(
        models.ProjectUpdate(
            actions=[models.ProjectChangeCountriesAction(countries=["AT", "NL"])],
            version=project.version,
        )
    )
    assert project.countries == ["AT", "NL"]


def test_project_update_change_messages_enabled(ct_platform_client: Client):
    project = ct_platform_client.with_project_key("unittest").get()
    assert project
    project = ct_platform_client.with_project_key("unittest").post(
        models.ProjectUpdate(
            actions=[models.ProjectChangeMessagesEnabledAction(messages_enabled=True)],
            version=project.version,
        )
    )
    assert project.messages.enabled is True


def test_project_update_change_country_tax_rate_fallback_enabled(
    ct_platform_client: Client,
):
    project = ct_platform_client.with_project_key("unittest").get()
    project = ct_platform_client.with_project_key("unittest").post(
        models.ProjectUpdate(
            actions=[
                models.ProjectChangeCountryTaxRateFallbackEnabledAction(
                    country_tax_rate_fallback_enabled=True
                )
            ],
            version=project.version,
        )
    )
    assert project.carts.country_tax_rate_fallback_enabled is True


def test_project_update_set_shipping_rate_input_type(ct_platform_client: Client):
    project = ct_platform_client.with_project_key("unittest").get()
    assert project.shipping_rate_input_type is None

    project = ct_platform_client.with_project_key("unittest").post(
        models.ProjectUpdate(
            actions=[
                models.ProjectSetShippingRateInputTypeAction(
                    shipping_rate_input_type=models.ShippingRateInputType(
                        type=models.ShippingRateTierType.CART_VALUE
                    )
                )
            ],
            version=project.version,
        )
    )
    assert project.shipping_rate_input_type == models.CartValueType()

    project = ct_platform_client.with_project_key("unittest").post(
        models.ProjectUpdate(
            actions=[
                models.ProjectSetShippingRateInputTypeAction(
                    shipping_rate_input_type=models.CartClassificationType(
                        values=[
                            models.CustomFieldLocalizedEnumValue(
                                key="test", label=models.LocalizedString({"en": "test"})
                            )
                        ]
                    )
                )
            ],
            version=project.version,
        )
    )
    assert project.shipping_rate_input_type == models.CartClassificationType(
        values=[
            models.CustomFieldLocalizedEnumValue(
                key="test", label=models.LocalizedString({"en": "test"})
            )
        ]
    )

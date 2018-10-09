from marshmallow import fields


class PredicateList(fields.List):
    """Join multiple predicates.

    If multiple predicates are specified via multiple where query parameters,
    the individual predicates are combined in a logical conjunction, just as
    if they had been specified in a single where query parameter and combined
    with and.
    """

    def serialize(self, attr, obj, accessor=None):
        result = super().serialize(attr, obj, accessor)
        if result:
            return " and ".join(result)
        return result

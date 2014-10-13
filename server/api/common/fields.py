from flask.ext.restful import fields


class DateTimeISO(fields.Raw):
    """Return a ISO 8601 datetime for datetime object"""

    def format(self, value):
        try:
            return value.isoformat()
        except AttributeError as e:
            raise fields.MarshallingException(e)

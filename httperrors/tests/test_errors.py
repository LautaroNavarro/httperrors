from httperrors.errors import BadRequestError


class TestErrors:

    def test_error_serializer_default_values(self):
        error = BadRequestError()
        expected_result = {
            "error_message": "Bad request.",
            "status_code": 400,
        }
        result = error.serialize()

        assert result == expected_result

    def test_error_serializer_default_values_custom_error_message(self):
        error = BadRequestError(
            error_message="Custom error message."
        )
        expected_result = {
            "error_message": "Custom error message.",
            "status_code": 400,
        }
        result = error.serialize()

        assert result == expected_result

    def test_error_serializer_include_error_code(self):
        error = BadRequestError()
        expected_result = {
            "error_message": "Bad request.",
            "status_code": 400,
            "error_code": None,
        }
        result = error.serialize(include_error_code=True)

        assert result == expected_result

    def test_error_serializer_include_error_code_custom_error_code(self):
        error = BadRequestError(
            error_code="INVALID_ENTITY_ID"
        )
        expected_result = {
            "error_message": "Bad request.",
            "status_code": 400,
            "error_code": "INVALID_ENTITY_ID",
        }
        result = error.serialize(include_error_code=True)

        assert result == expected_result

    def test_error_serializer_not_include_status_code(self):
        error = BadRequestError(
            error_code="INVALID_ENTITY_ID"
        )
        expected_result = {
            "error_message": "Bad request.",
        }
        result = error.serialize(include_status_code=False)

        assert result == expected_result

    def test_error_serializer_not_include_status_code_and_include_error_code(
        self
    ):
        error = BadRequestError(
            error_code="INVALID_ENTITY_ID"
        )
        expected_result = {
            "error_message": "Bad request.",
            "error_code": "INVALID_ENTITY_ID",
        }
        result = error.serialize(
            include_status_code=False,
            include_error_code=True,
        )

        assert result == expected_result

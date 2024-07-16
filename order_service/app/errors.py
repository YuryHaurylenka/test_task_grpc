from fastapi import HTTPException, status


def handle_integrity_error():
    """Handle integrity errors such as unique constraint violations."""
    detail_msg = (
        "A database integrity error occurred. This might be due to unique constraints."
    )
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail_msg)


def handle_database_error():
    """Handle general database errors."""
    detail_msg = (
        "An internal server error occurred while interacting with the database."
    )
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail_msg
    )


def handle_not_found_error(detail: str | None):
    """Handle not found errors."""
    detail_msg = "The requested order was not found."
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail_msg)


def handle_unexpected_error(detail: str | None):
    """Handle unexpected errors."""
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail
    )


def handle_user_not_found_error(detail: str | None):
    """Handle user not found errors."""
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

from fastapi import HTTPException

class TodoCreationError(HTTPException):
    def __init__(self, detail: str = "Failed to create todo"):
        super().__init__(status_code=500, detail=detail)

class TodoNotFoundError(HTTPException):
    def __init__(self, detail: str = "Todo not found"):
        super().__init__(status_code=404, detail=detail)

class TodoUpdateError(HTTPException):
    def __init__(self, detail: str = "Failed to update todo"):
        super().__init__(status_code=500, detail=detail)

class TodoDeletionError(HTTPException):
    def __init__(self, detail: str = "Failed to delete todo"):
        super().__init__(status_code=500, detail=detail)

class UserError(HTTPException):
    def __init__(self, detail: str = "User error"):
        super().__init__(status_code=400, detail=detail)

class UserNotFoundError(HTTPException):
    def __init__(self, detail: str = "User not found"):
        super().__init__(status_code=404, detail=detail)

class passwordError(HTTPException):
    def __init__(self, detail: str = "Password error"):
        super().__init__(status_code=400, detail=detail)

class PasswordsDoNotMatchError(HTTPException):
    def __init__(self, detail: str = "Password mismatch"):
        super().__init__(status_code=400, detail=detail)

class AuthenticationError(HTTPException):
    def __init__(self, detail: str = "Authentication failed"):
        super().__init__(status_code=401, detail=detail)

class invalidPasswordError(HTTPException):
    def __init__(self, detail: str = "Invalid password"):
        super().__init__(status_code=400, detail=detail)
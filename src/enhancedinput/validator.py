from urllib.parse import urlparse
import re

class Validator:
    def valid(self, value: str):
        raise NotImplementedError("You must implement valid() in your validator class")


class Validators:
    class BlankValidator(Validator):
        def valid(self, value: str):
            return True
        
    class BooleanValidator(Validator):
        hint = "y/n"

        def valid(self, value: str):
            return value.lower() in ["true", "false", "1", "0", "yes", "no", "y", "n", "t", "f"]

    class IntValidator(Validator):
        hint = "integer"

        def valid(self, value: str):
            try:
                int(value)
                return True
            except ValueError:
                return False

    class FloatValidator(Validator):
        hint = "float"

        def valid(self, value: str):
            try:
                float(value)
                return True
            except ValueError:
                return False

    class EmailValidator(Validator):
        hint = "email"

        def __init__(self) -> None:
            self.regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            self.p = re.compile(self.regex)

        def valid(self, value: str):
            return self.p.match(value) is not None

    class URLValidator(Validator):
        hint = "url"

        def valid(self, value: str):
            parsed = urlparse(value)
            return parsed.scheme != "" and parsed.netloc != ""
        
    class RangeValidator(Validator):
        def __init__(self, min: float | int, max: float | int, mode: int | float = int) -> None:
            self.mode = mode
            self.min = self.mode(min)
            self.max = self.mode(max)

            self.hint = f"{self.min} - {self.max}"

        def valid(self, value: str):
            try:
                return self.min <= self.mode(value) <= self.max
            except ValueError:
                return False
    
    class LengthValidator(Validator):
        def __init__(self, min: int, max: int = None) -> None:
            self.min = min
            self.max = max

            self.hint = f"{self.min} - {self.max}" if self.max is not None else f"{self.min}+"

        def valid(self, value: str):
            return self.min <= len(value) <= (self.max if self.max is not None else len(value))

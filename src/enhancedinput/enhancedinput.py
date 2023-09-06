from .themes import Themes, Theme
from .colors import Colors
from .validator import Validator
import sys

class EnhancedInput:
    def __init__(self, theme: Theme = Themes.default) -> None:
        self.theme: Theme = theme
        self.invalid_input_message: str = Colors.RED + "Invalid input" + Colors.END

    """Get input from the user"""
    def get(self, prompt: str = "", theme: Theme = None, validators: list[Validator] = []) -> str:
        if theme is None:
            theme = self.theme
            
        hints = []
        for validator in validators:
            try:
                hints.append(validator.hint)
            except AttributeError:
                pass

        while True:
            res = input(theme.format(prompt, hints))

            for validator in validators:
                if not validator.valid(res):
                    print(self.invalid_input_message)
                    break
            else:
                break
    
        sys.stdout.write(Colors.END)
        sys.stdout.flush()

        return res

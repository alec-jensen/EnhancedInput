from .colors import Colors

class Theme:
    def __init__(self, prefix: str = "", suffix: str = "") -> None:
        self.prefix = prefix
        self.suffix = suffix

    """Format text with the theme's prefix and suffix"""
    def format(self, text: str, hints: list[str] = []) -> str:
        return f"{self.prefix}{text} ({', '.join(hints)}){self.suffix}"

class Themes:
    default = Theme(suffix=": ")
    fancy = Theme(prefix=f"{Colors.CYAN}", suffix=f"{Colors.END}\n{Colors.BOLD + Colors.LIGHT_WHITE}> ")
from src.enhancedinput import EnhancedInput, Themes, Validators

inp = EnhancedInput(theme=Themes.fancy)

name = inp.get("What is your name?", validators=[Validators.LengthValidator(1, 20)])

print(f"Hello, {name}!")

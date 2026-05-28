import pyfiglet
from rich.console import Console
from rich.align import Align
from rich.text import Text

console = Console()

linha1 = pyfiglet.figlet_format("Global Solution", font="ansi_shadow")
linha2 = pyfiglet.figlet_format("Mission Control AI", font="ansi_shadow")


console.print(Align.center(Text(linha1, style="bold cyan")))
console.print(Align.center(Text(linha2, style ="bold purple")))

console.print(Align.center(
    Text("── 2026.1 . Prompt Engineering and AI . FIAP ──", style="italic bright_black")
))
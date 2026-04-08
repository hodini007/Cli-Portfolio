import sys
import time
import os

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.table import Table
    from rich import box
    from rich.progress import track
except ImportError:
    print("This resume requires the 'rich' library to render beautiful terminal elements.")
    print("Please install it by running: pip install rich")
    sys.exit(1)

# Ensure UTF-8 output for Windows console and characters
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

if os.name == 'nt':
    os.system('chcp 65001 >nul')

console = Console()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_line(text, delay=0.015, newline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

banner_name = r"""
          _____                    _____                    _____                _____                    _____                    _____          
         /\    \                  /\    \                  /\    \              |\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \             |:\____\                /::\    \                /::\____\        
       /::::\    \              /::::\    \               \:::\    \            |::|   |               /::::\    \              /::::|   |        
      /::::::\    \            /::::::\    \               \:::\    \           |::|   |              /::::::\    \            /:::::|   |        
     /:::/\:::\    \          /:::/\:::\    \               \:::\    \          |::|   |             /:::/\:::\    \          /::::::|   |        
    /:::/__\:::\    \        /:::/__\:::\    \               \:::\    \         |::|   |            /:::/__\:::\    \        /:::/|::|   |        
   /::::\   \:::\    \      /::::\   \:::\    \              /::::\    \        |::|   |           /::::\   \:::\    \      /:::/ |::|   |        
  /::::::\   \:::\    \    /::::::\   \:::\    \    ____    /::::::\    \       |::|___|______    /::::::\   \:::\    \    /:::/  |::|   | _____  
 /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /\   \  /:::/\:::\    \      /::::::::\    \  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \ 
/:::/  \:::\   \:::|    |/:::/  \:::\   \:::\____\/::\   \/:::/  \:::\____\    /::::::::::\____\/:::/  \:::\   \:::\____\/:: /    |::|   /::\____\
\::/   |::::\  /:::|____|\::/    \:::\  /:::/    /\:::\  /:::/    \::/    /   /:::/~~~~/~~      \::/    \:::\  /:::/    /\::/    /|::|  /:::/    /
 \/____|:::::\/:::/    /  \/____/ \:::\/:::/    /  \:::\/:::/    / \/____/   /:::/    /          \/____/ \:::\/:::/    /  \/____/ |::| /:::/    / 
       |:::::::::/    /            \::::::/    /    \::::::/    /           /:::/    /                    \::::::/    /           |::|/:::/    /  
       |::|\::::/    /              \::::/    /      \::::/____/           /:::/    /                      \::::/    /            |::::::/    /   
       |::| \::/____/               /:::/    /        \:::\    \           \::/    /                       /:::/    /             |:::::/    /    
       |::|  ~|                    /:::/    /          \:::\    \           \/____/                       /:::/    /              |::::/    /     
       |::|   |                   /:::/    /            \:::\    \                                       /:::/    /               /:::/    /      
       \::|   |                  /:::/    /              \:::\____\                                     /:::/    /               /:::/    /       
        \:|   |                  \::/    /                \::/    /                                     \::/    /                \::/    /        
         \|___|                   \/____/                  \/____/                                       \/____/                  \/____/         
"""

PHOTO_ASCII = r"""
                                                                                                                
                                                                                                                
                                              ▒                                                                
                                            ░▒▓   ░ ▒░                                                         
                                          ░       ░░     ░░                                                    
                                         ▒ ░         ░▒█░ ░▒                                                   
                                        ░░      ░░░░▒░░▒▒▓▓▒░▓                                                 
                                        ░  ░░░░░░░░░░ ░░   ░ ░                                                 
                                       ░ ░░░░░░░░░░░▒▓█▓▓░░                                                    
                                         ░▓▓█▓▒▒▒▒░░ ░░░░▒▓░ ░                                                 
                                         ░▓   ░░░░░░░░ ▒░░░▒                                                   
                                        ░░░░▒░░░ ░░▒░░░░░▒░▒▒▓▒░░                                              
                                         ▒▒▒▒░ ░▓▓░ ░░░░░░░▒░▒░                                                
                                       █▒▒▒▒▒▓▒░▓▒░░▒░░░░░░░░▒░░                                               
                                       ░░░▒▒░░░░░░░░░░░░░░░░▒▒░                                                
                                          ░▒░░░▓▒░░░░░ ░░░░░░▒                                                 
                                           ░▒░░░ ░░░░░░░░░░░░▒                                                 
                                             ░▒░▒▒░░░░░░░░░░░░                                                 
                                              ▒░░░░░░░░░░░░░░░                                                 
                                              ░▒▒▒░░░░░░░░░░░░                                                 
                                               ░░▒░░░░░░░░░░░▓                                                 
                                              ░░░▒▒▒▒░░░░░░░░▒                                                 
                                              ▒░░░░░░░░░░░░░░▒░                                                
                                              ▒▒░ ░░░░░░░░░ ▒▒▒░                                               
                                           ░▒░░▒▒▒▒   ░░  ░▓▒▒░░░▒░                                            
                                        ░░░░░░░░░▒▒▓█▓░░▒█▓▒▒░░░░░░░░▒░                                        
                                    ░░░░░░░░░░░░░░▒▓▒      ▓▓▒░░░░░░░░░░░░░                                    
                                ░▒░▒░░░░░░░░░░░░▒▒▒          ▒░░░░░░░░░░░░░░░░░                                
                             ▒░░░░░░░░░░░░░▒▒▒▒░▒░░▒▒▒      ▓▒░░░░░░░░░░░░░░░░░░▒▒                             
                            ▒░░░░░░░░░░░░░░▒░░▒▒▒▒▒▒▒▒▒░   ░▓▒░░░▒▒▒░░░░░░░░░░░░░░░                            
                           ▒▒░░░░░░▒▒▒░░░░▒▒░░░▒▒░▒▒▒░▒     ▓▒░░░▒░▒░░░░░░░░░░░░░░░▒                           
                          ▒▒░░░░▒▒▒▒░▒▒░░░▒░░░░░▒▒░▒▒▒░     ▒▒░░░▒░▒░░░░▒░▒░░░░░░░░░▒                          
                          ░░░░▒▒▒░▒▒░░▒▒░░▒░░░░░▒▒▒░▒▒░     ░▒▒░░▒▒▒░░░░░░░░░░░░░░░░▒▒                         
                         ▒░░░░▒░░▒▒▒▒░░▒▒░▒░░░░░▒░▒▒░▒░     ░▒▒░░░░░░░░░▒░▒░░░░░░░░░░▒                         
                         ▒░░░░▒░░░▒░░░░▒▒▒▒░░░░▒▒░▒▒▒░      ░░▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░▒                         
                         ▒░░░░▒░▒░░░░▒░░▒▒▒▒░░░▒░░▒▒▒▒      ░▒▒▒░░░░░░▒░▒░░▒░░▒░▒░░░░▒                         
                         ▒░░░░▒▒░▒░░░▒▒░░▒▒▒▒░░▒░░▒░▒▒       ▒▒▒░░░░░░▒░▒▒░▒░▒▒▒▒░░░░░░                        
                         ▒░░░░░▒░░▒░░░▒░░░▒▒▒▒░▒░░▒░░▒░▒▒██▓▒▒▒░░░░░░░▒▒▒▒▒▒░▒▒░░░░░░░░                        
                         ▒░░░░▒▒░▒▒▒░░▒░░░▒▒▒▒▒▒░░▒▒▒░    ░  ▒▒▒░░░░▒▒▒▒░░▒░░▒▒░░░░░░░░                        
                         ░░░░▒▒▒▒▒▒▒▒░░▒░░░▒▒░▒▒▒▒▒▒▒▒       ░▒▒▒▒▒░▒░    ▒░░▒▒░░░░░░░░                        
                         ░░░▒▒▒░░▒  ░░░░▒░░▒▒░░░░▒░░░▒       ░░▒▒░▒▒▒▒▒▒▒▒░░░▒▒░░░░░░░░                        
                         ░░░▒▒░░  ░░░░░░▒░░▒▒▒▒░░░░░ ░       ▒░▒▒░░▒▒▒▒▒▒░▒░░▒▒░░░░░░░░                        
                         ▒░░▒▒░ ░░░░░░░░░░░░▒░░░░░░░░▓       ▒░░▒▒░░▒▒▒▒░░░  ▒▒▒░░░░░░░▒                       
                         ▒░░░▒▒░░░░░░░░░   ░▒▒░▒▒▒▒▒▒▓      ░▓▒░▒▒░░░░░░░░   ▒▒▒▒░░░░░░▒░                      
                         ░░░░░▒▒░ ░░░░░░    ░▒▓▓▒▒▒▒▒░      ░▒▒░░░░░░      ░  ▒▒▒░░░░░░░▒                      
                         ▒░░░░▒▒▒▒    ░▒▓▓▓▒░       ░       ░░▒▒▒▒▒▒▒▓▓▓▓▒░░░ ░▒▒░░░░░░░█                      
                         ▒░░░░░▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▒▓▓▓█████▓▓▒░░░░░▒▒▒▒░░░░░░ ▒▒░░░░░░░░                      
                         ░░░░░▒░░▒▒░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░   ░▒▒░░░░░░░░                      
                          ░░░░░░▒░▒░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░    ░▓▓▒▒░░░░░░░░░                      
                          ▒░░░▒▒░▒▒░░░▒▒▒░░░░▒▒▒░░░░░░░░░░░░░░▒▒▒▒░░░░▓▓▓▓▓▒▒░░░░░░░░░░░░                      
                          ▒░░░▒░▒▒░░░░▒░▒░░░▒▒▒░░░░░░░░░░▒▒▒░░    ░█▓▒▒░░░░░░▒▒▒▒▒▒▒▒░░░░                      
                          ░░▒░▒▒▒░░░░░▒▒▒░░▒▒░░░░░░░░░░░     ░░░░░░  ▓▒▒▒░░░░▒░░░░░░░░░░░                      
                            ▒░░░░░░░░░░░░░▒▒░░░░░░░░ ░░░░░░░░░░░░░░░░░ ▓▒▒▒░░▒▒▒▒▒▒▒▒░░░                       
                            ▓█▒▒▒▒░░░░░░░░▒  ░░░▓▒░▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒░▒▒▒░░░░░░░                        
                                 ░░░░░▒▒▒▒▒▒▒▒▒▒░░░    ░░░░    ░░░░░░░░░   ▒▒▒░▒░▒░                            
                                 ▒░░░░▒░░░▒▒▒░▒░░░        ▒▒▒▒▒▓▒░░   ▒▓▓▓▒▒▒░▒▒░                              
                                 ░░░░░▒▒▒▒▒░▒▒▒▒▒▓        ████▓▓▒▒▒▓▓▒▒░░░░▒▒▒▒▒░▒                             
                                ░░░░░░░░░░░░░░░▒▒▓              ▓▓▓▓▓▓▒▒▒░░▒░░░                                
                                ░░░░░░░░░▒▒▒▒▒▓▓▓▒       ░▓▓▓▓░     ░░▒▓▓▓██▓▒▒                                
                               ▒░▒▒▒▒▒▓▓██▓▓▒░░░░░▒░   ░▒▒░░░░░░             ░░                                
"""

EMAIL = "[link=mailto:raiyanrohit10@gmail.com]raiyanrohit10@gmail.com[/link]"
LINKEDIN = "[link=https://linkedin.com/in/YOUR_LINKEDIN]LinkedIn[/link]"
GITHUB = "[link=https://github.com/hodini007]GitHub[/link]"

PROFILE = f"""
[bold cyan]>>[/] [bold white]MD. Raiyan Bin Rafique[/]
[bold cyan]>>[/] [bright_black]Undergraduate Computer Science Student[/]
[bold cyan]>>[/] [bright_black]{EMAIL} | +8801870134818 | {LINKEDIN} | {GITHUB}[/]
[bold cyan]>>[/] [bright_black]Rajshahi, Bangladesh[/]
"""

PROFILE_SUMMARY = """
[bright_black]Dedicated Computer Science and Engineering student at Rajshahi University of Engineering 
& Technology (RUET) with a strong foundation in Machine Learning (ML), Python, Julia, 
and practical AI/Automation projects. Actively seeking research opportunities to apply 
growing knowledge in coding and technical skills, highlighted by high academic achievement 
(CGPA 3.88 in 1st Year) and experience in the research and development wing of the 
Notre Dame Science Club.[/]
"""

def print_education():
    table = Table(title="[bold yellow]EDUCATION[/]", box=box.SIMPLE, show_header=False)
    
    table.add_row(
        "[bold cyan]Rajshahi University of Engineering & Technology (RUET)[/]\n[magenta]B.Sc. in Computer Science and Engineering[/]\n[bright_black]CGPA: 3.88/4.00 | June 2024 – Present[/]"
    )
    table.add_row(" ")
    table.add_row(
        "[bold cyan]Notre Dame College, Dhaka[/]\n[bright_black]Higher Secondary Certificate (Science), GPA: 5.00/5.00 | 2022 – 2024[/]"
    )
    table.add_row(" ")
    table.add_row(
        "[bold cyan]Domar Multilateral High School, Domar[/]\n[bright_black]Secondary School Certificate (Science), GPA: 5.00/5.00 | 2020 – 2022[/]"
    )
    console.print(Panel(table, border_style="cyan"))

def print_research():
    res = """
[bold cyan]Member, Research & Development Wing, Notre Dame Science Club, Dhaka[/]
[bright_black]Oct 2022 – Dec 2023[/]

[green]•[/] [bright_black]Engaged in early-stage research activities and experimental design.[/]
[green]•[/] [bright_black]Built a foundation in scientific inquiry and practical application of knowledge.[/]
    """
    console.print(Panel(res.strip(), title="[bold yellow]RESEARCH & TECHNICAL EXPERIENCE[/]", title_align="left", border_style="cyan"))

def print_skills():
    table = Table(title="[bold yellow]TECHNICAL SKILLS & FOCUS AREAS[/]", box=box.MINIMAL_DOUBLE_HEAD)
    table.add_column("Category", style="bold magenta")
    table.add_column("Skills", style="bright_black")

    table.add_row("Programming", "Python, Julia, C, basic scripting")
    table.add_row("ML/Data Tools", "NumPy, Pandas, Scikit-learn, TensorFlow, Keras")
    table.add_row("ML/AI Concepts", "Supervised Learning, Generative AI, Automation, CNN, Deep Learning")
    table.add_row("Tools/Libraries", "Multisim, Tkinter, pywinauto, Streamlit, Matplotlib, CustomTkinter, Skyfield, Requests")
    table.add_row("Other", "Data Visualization, Orbital Mechanics, SPICE Netlist, Google Gemini API")
    
    console.print(table)

def print_certifications():
    certs = """
[green]•[/] [bright_black]CS50x: Introduction to Computer Science (Harvard)[/]
[green]•[/] [bright_black]Machine Learning with Python (V2)[/]
[green]•[/] [bright_black]Introduction to Generative AI[/]
[green]•[/] [bright_black]Ethics in the Age of Generative AI[/]
    """
    console.print(Panel(certs.strip(), title="[bold yellow]CERTIFICATIONS[/]", title_align="left", border_style="cyan"))

def print_projects():
    console.print("\n[bold yellow][ KEY TECHNICAL PROJECTS ][/]")
    
    projects = [
        ("Elecsyn (AI Multisim Automation Agent)",
         "Developed a Python script that uses Google Gemini 2.5 Pro to generate SPICE netlists from natural language prompts, automatically importing and running simulations in NI Multisim via Python automation (pywinauto). Implements retry logic with exponential backoff. Demonstrates AI integration and end-to-end system automation."),
        
        ("Potato Disease Detection System (CNN)", 
         "Built an AI-powered Streamlit web application that classifies potato leaf diseases (Early Blight, Late Blight, Healthy) using a custom CNN trained on the PlantVillage dataset. Features 256×256 RGB inputs with built-in normalization, Conv2D and MaxPooling2D layers, and dual-input modes (file upload and live camera feed). Architecture is extensible to 10+ plant species."),
         
        ("OrbiSense (Satellite Tracking Application)",
         "Developed an interactive satellite tracking suite using the Skyfield SGP4 physics engine to predict passes and visualize ground-tracks for Weather satellites, ISS, Starlink, and Amateur Radio. Modular design with TLE caching, root-finding for precise horizon-crossing calculations, and a threaded CustomTkinter dark-mode UI with embedded Matplotlib 2D maps."),
         
        ("Diabetes Risk Classifier (ML/GUI)",
         "Created a GUI-based Prediction Application using ML to forecast diabetes risk based on user inputs (Age, BMI, Blood Pressure). Focused on user-friendly ML deployment."),
         
        ("Charged Particle Orbit Simulation (Julia)",
         "Simulated two charged particles under Coulomb's Law using Julia and numerical integration (Euler's method). Produced animated orbit visualizations using Plots.jl.")
    ]
    
    for name, desc in projects:
        panel = Panel(f"[bright_black]{desc}[/]", title=f"[bold cyan]{name}[/] - {GITHUB}", title_align="left", border_style="cyan")
        console.print(panel)
        time.sleep(0.3)

def main():
    clear_terminal()
    
    sys.stdout.write('\033[38;2;0;255;255m')  # Cyan ANSI
    type_line("INITIALIZING SECURE CONNECTION...", delay=0.03)
    type_line("ESTABLISHING HANDSHAKE...", delay=0.03)
    type_line("ACCESS GRANTED.", delay=0.03)
    time.sleep(0.4)
    sys.stdout.write('\033[0m')  # Reset ANSI
    
    # Use standard print for banner and ASCII since they are raw preformatted art
    print('\033[38;2;0;255;255m' + banner_name + '\033[0m')
    time.sleep(0.3)

    print(PHOTO_ASCII)
    time.sleep(0.4)
    
    console.print(Panel(PROFILE.strip(), title="[bold yellow]SYSTEM IDENTIFICATION[/]", border_style="cyan"))
    time.sleep(0.4)

    console.print(Panel(PROFILE_SUMMARY.strip(), title="[bold yellow]PROFILE SUMMARY[/]", border_style="cyan"))
    time.sleep(0.4)

    print_education()
    time.sleep(0.3)

    print_research()
    time.sleep(0.3)
    
    print_skills()
    time.sleep(0.4)

    print_certifications()
    time.sleep(0.3)
    
    # Progress Bar using rich track
    print()
    sys.stdout.write('\033[1m\033[38;2;0;255;255mLOADING PROJECT DATA PACKETS\033[0m\n')
    for step in track(range(100), description="[cyan]Extracting..."):
        time.sleep(0.015)
    print()
    
    print_projects()
    time.sleep(0.5)
    
    console.print("\n[bold green][SYSTEM HACK COMPLETED: Enjoy exploring Raiyan's Portfolio][/]")
    
    console.print("\n[bright_black]Press Enter to exit...[/]")
    try:
        input()
    except EOFError:
        pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]CONNECTION TERMINATED.[/]")
        sys.exit(0)

import sys
import time
import os

# Ensure UTF-8 output for Windows console and characters
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Enable ANSI colors for Windows terminal
os.system('')

# Terminal Colors (ANSI)
CYAN = '\033[38;2;0;255;255m'
PURPLE = '\033[38;2;170;0;255m'
GREEN = '\033[38;2;57;255;20m'
YELLOW = '\033[38;2;250;250;50m'
WHITE = '\033[38;2;255;255;255m'
GRAY = '\033[38;2;150;150;150m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def make_link(text, url):
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"

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

banner_photo = f"""
{CYAN}                                                                                                               
                                                                                                               
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
                               ▒░▒▒▒▒▒▓▓██▓▓▒░░░░░▒░   ░▒▒░░░░░░             ░░{RESET}
"""

EMAIL = make_link("raiyanrohit10@gmail.com", "mailto:raiyanrohit10@gmail.com")
LINKEDIN = make_link("LinkedIn", "https://linkedin.com/in/YOUR_LINKEDIN")
GITHUB = make_link("GitHub", "https://github.com/hodini007")

PROFILE = f"""
{BOLD}{CYAN}>> {WHITE}MD. Raiyan Bin Rafique{RESET}
{CYAN}>> {GRAY}Undergraduate Computer Science Student{RESET}
{CYAN}>> {GRAY}{EMAIL} | +8801870134818 | {LINKEDIN} | {GITHUB}{RESET}
{CYAN}>> {GRAY}Rajshahi, Bangladesh{RESET}
"""

PROFILE_SUMMARY = f"""
{BOLD}{YELLOW}[ PROFILE SUMMARY ]{RESET}
{GRAY}Dedicated Computer Science and Engineering student at Rajshahi University of Engineering 
& Technology (RUET) with a strong foundation in Machine Learning (ML), Python, Julia, 
and practical AI/Automation projects. Actively seeking research opportunities to apply 
growing knowledge in coding and technical skills, highlighted by high academic achievement 
(CGPA 3.88 in 1st Year) and experience in the research and development wing of the 
Notre Dame Science Club.{RESET}
"""

EDUCATION = f"""
{BOLD}{YELLOW}[ EDUCATION ]{RESET}
 {BOLD}{CYAN}Rajshahi University of Engineering & Technology (RUET), Rajshahi{RESET}
 {PURPLE}B.Sc. in Computer Science and Engineering{RESET}
 {GRAY}CGPA: 3.88/4.00 (1st Year Odd Semester) | June 2024 – Present{RESET}

 {BOLD}{CYAN}Notre Dame College, Dhaka{RESET}
 {GRAY}Higher Secondary Certificate (Science), GPA: 5.00/5.00 | 2022 – 2024{RESET}

 {BOLD}{CYAN}Domar Multilateral High School, Domar{RESET}
 {GRAY}Secondary School Certificate (Science), GPA: 5.00/5.00 | 2020 – 2022{RESET}
"""

RESEARCH = f"""
{BOLD}{YELLOW}[ RESEARCH & TECHNICAL EXPERIENCE ]{RESET}
 {BOLD}{CYAN}Member, Research & Development Wing, Notre Dame Science Club, Dhaka{RESET}
 {GRAY}Oct 2022 – Dec 2023{RESET}
 {GREEN}• {GRAY}Engaged in early-stage research activities and experimental design.
 {GREEN}• {GRAY}Built a foundation in scientific inquiry and practical application of knowledge.{RESET}
"""

SKILLS = f"""
{BOLD}{YELLOW}[ TECHNICAL SKILLS & FOCUS AREAS ]{RESET}
 {BOLD}{PURPLE}Programming:{RESET}     {GRAY}Python, Julia, basic data/scripting languages{RESET}
 {BOLD}{PURPLE}ML/Data Tools:{RESET}   {GRAY}NumPy, Pandas, Scikit-learn, TensorFlow, Keras{RESET}
 {BOLD}{PURPLE}ML/AI Concepts:{RESET}  {GRAY}Supervised Learning, Generative AI, Predictive Modeling, Automation,
                  CNN, Deep Learning{RESET}
 {BOLD}{PURPLE}Tools/Libraries:{RESET} {GRAY}Multisim, Tkinter, pywinauto, Streamlit, Matplotlib, CustomTkinter, 
                  Skyfield, Requests{RESET}
 {BOLD}{PURPLE}Other:{RESET}           {GRAY}Data Visualization (Python/Julia), Orbital Mechanics, SPICE Netlist, 
                  Google Gemini API{RESET}
"""

CERTIFICATIONS = f"""
{BOLD}{YELLOW}[ CERTIFICATIONS ]{RESET}
 {GREEN}• {GRAY}CS50x: Introduction to Computer Science (Harvard){RESET}
 {GREEN}• {GRAY}Machine Learning with Python (V2){RESET}
 {GREEN}• {GRAY}Introduction to Generative AI{RESET}
 {GREEN}• {GRAY}Ethics in the Age of Generative AI{RESET}
"""

PROJECTS = f"""
{BOLD}{YELLOW}[ KEY TECHNICAL PROJECTS ]{RESET}

 {BOLD}{CYAN}Elecsyn (AI Multisim Automation Agent){RESET} — {GITHUB}
 {GRAY}Developed a Python script that uses Google Gemini 2.5 Pro to generate SPICE netlists 
 from natural language prompts, automatically importing and running simulations in 
 NI Multisim via Python automation (pywinauto). Implements retry logic with exponential 
 backoff. Demonstrates AI integration and end-to-end system automation.{RESET}

 {BOLD}{CYAN}Potato Disease Detection System (CNN/Deep Learning){RESET} — {GITHUB}
 {GRAY}Built an AI-powered Streamlit web application that classifies potato leaf diseases 
 (Early Blight, Late Blight, Healthy) using a custom CNN trained on the PlantVillage 
 dataset. Features 256×256 RGB inputs with built-in normalization, Conv2D and MaxPooling2D 
 layers, and dual-input modes (file upload and live camera feed). Architecture is extensible 
 to 10+ plant species.{RESET}

 {BOLD}{CYAN}OrbiSense (Satellite Tracking Application){RESET} — {GITHUB}
 {GRAY}Developed an interactive satellite tracking suite using the Skyfield SGP4 physics engine 
 to predict passes and visualize ground-tracks for Weather satellites, ISS, Starlink, 
 and Amateur Radio. Modular design with TLE caching (24-hour TTL), root-finding for precise 
 horizon-crossing calculations, and a threaded CustomTkinter dark-mode UI with embedded 
 Matplotlib 2D maps. Originally built to intercept weather-satellite telemetry during 
 severe cyclones.{RESET}

 {BOLD}{CYAN}Diabetes Risk Classifier (ML/GUI){RESET} — {GITHUB}
 {GRAY}Created a GUI-based Prediction Application using ML to forecast diabetes risk based on 
 user inputs (Age, BMI, Blood Pressure). Focused on user-friendly ML deployment.{RESET}

 {BOLD}{CYAN}Charged Particle Orbit Simulation (Julia/Physics){RESET} — {GITHUB}
 {GRAY}Simulated two charged particles under Coulomb’s Law using Julia and numerical integration 
 (Euler’s method). Produced animated orbit visualizations using Plots.jl.{RESET}
"""

def main():
    clear_terminal()
    
    sys.stdout.write(CYAN)
    type_line("INITIALIZING SECURE CONNECTION...", delay=0.03)
    type_line("ESTABLISHING HANDSHAKE...", delay=0.03)
    type_line("ACCESS GRANTED.", delay=0.03)
    time.sleep(0.4)
    sys.stdout.write(RESET)
    
    print(CYAN + banner_name + RESET)
    time.sleep(0.3)
    
    print(banner_photo)
    time.sleep(0.3)
    
    print(PROFILE)
    time.sleep(0.4)

    print(PROFILE_SUMMARY)
    time.sleep(0.4)

    print(EDUCATION)
    time.sleep(0.3)

    print(RESEARCH)
    time.sleep(0.3)
    
    print(SKILLS)
    time.sleep(0.4)

    print(CERTIFICATIONS)
    time.sleep(0.3)
    
    sys.stdout.write(BOLD + CYAN + "LOADING PROJECT DATA PACKETS" + RESET)
    for _ in range(3):
        sys.stdout.write(CYAN + "." + RESET)
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n")
    
    print(PROJECTS)
    time.sleep(0.5)
    
    type_line(f"{GREEN}[SYSTEM HACK COMPLETED: Enjoy exploring Raiyan's Portfolio]{RESET}", delay=0.01)
    
    print(f"\n{GRAY}Press Enter to exit...{RESET}")
    input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{GREEN}CONNECTION TERMINATED.{RESET}")
        sys.exit(0)

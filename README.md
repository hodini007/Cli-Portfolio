# 🚀 Interactive CLI Portfolio

Welcome to my interactive, terminal-based portfolio! This project allows you to view my resume, skills, and projects directly from your command line interface. It features custom ASCII art, a retro-futuristic "hacker" typing animation, and beautiful styling powered by the `rich` Python library.

![portfolio screenshot](https://via.placeholder.com/800x400.png?text=CLI+Portfolio+Screenshot) *(Note: You can replace this placeholder image with an actual screenshot of your terminal later!)*

## ⚡ How to Run

You don't need to manually download or save any files. If you have Python installed, simply open your terminal (Command Prompt, PowerShell, or bash) and paste the following command. It will automatically install the `rich` UI library and run the interactive portfolio from the `rich_implementation` branch!

### Windows (Command Prompt):
```cmd
pip install rich && curl -sL https://raw.githubusercontent.com/hodini007/cli-portfolio/rich_implementation/portfolio.py | python
```

### Windows (PowerShell):
```powershell
pip install rich; curl.exe -sL https://raw.githubusercontent.com/hodini007/cli-portfolio/rich_implementation/portfolio.py | python
```

### Mac / Linux:
```bash
pip3 install rich && curl -sL https://raw.githubusercontent.com/hodini007/cli-portfolio/rich_implementation/portfolio.py | python3
```

## 🛠️ Features
- **Instant Execution:** Automatically fetches and runs via `curl` straight into Python memory. 
- **Rich Terminal UI:** Displays skills and projects using clean tables, bordered panels, and formatting.
- **Dynamic Progress Bars:** Features smooth, animated data-loading terminal bars.
- **Typewriter Animation:** Retro, delayed text printing for the boot-up sequence.
- **ASCII Art:** Custom generated 3D name banner and portrait art.
- **Cross-Platform:** Works successfully on Windows, macOS, and Linux out of the box with proper ANSI support encoding (`chcp 65001`).
- **Clickable Links:** Uses modern terminal hyperlinking for my email, LinkedIn, and GitHub profiles.

## 👨‍💻 About Me
I'm MD. Raiyan Bin Rafique, an undergraduate Computer Science student at Rajshahi University of Engineering & Technology (RUET). I have a strong focus on Machine Learning, Python, and AI Automation.

---
*Created by [MD. Raiyan Bin Rafique](https://github.com/hodini007)*

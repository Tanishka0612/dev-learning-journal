print("Common Git Commands")

commands = {
    "git init": "Start a new repository",
    "git add .": "Add files to staging",
    "git commit -m": "Save changes",
    "git push": "Upload code to GitHub"
}

for command, description in commands.items():
    print(f"{command} → {description}")

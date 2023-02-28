import os
import glob


def is_deep(path):
    return [os.path.basename(file) for file in glob.glob(f"{path}\\deep*")]


inp = input("Enter your path\n")
print(is_deep(inp))

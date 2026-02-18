"""
setup.py — Run this FIRST before opening the Jupyter Notebook.
Installs all required libraries for the IMDB Transformer project.
"""
import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


required = {
    "torch":         "torch",
    "datasets":      "datasets",
    "sklearn":       "scikit-learn",
    "matplotlib":    "matplotlib",
    "seaborn":       "seaborn",
    "numpy":         "numpy",
    "pandas":        "pandas",
    "notebook":      "notebook",
}

print("=" * 55)
print("  IMDB Transformer Project — Environment Setup")
print("=" * 55)
print(f"\nPython: {sys.version}\n")

for import_name, pip_name in required.items():
    try:
        __import__(import_name)
        print(f"  ✓ {pip_name} already installed")
    except ImportError:
        print(f"  Installing {pip_name}...")
        install(pip_name)
        print(f"  ✓ {pip_name} installed")

print("\n" + "=" * 55)
print("  All libraries ready!")
print("  Launch the notebook with:")
print("    jupyter notebook imdb_transformer_project.ipynb")
print("=" * 55)

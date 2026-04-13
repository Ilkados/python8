import sys
import importlib

def check_dependencies():
    """Checks if required packages are installed and prints their versions."""
    packages = ["pandas", "numpy", "matplotlib", "requests"]
    missing = []
    
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    
    for pkg in packages:
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {pkg} ({version}) - Ready")
        except ImportError:
            print(f"[MISSING] {pkg}")
            missing.append(pkg)
    
    if missing:
        print("\nError: Missing dependencies detected.")
        print("To install with pip: pip install -r requirements.txt")
        print("To install with Poetry: poetry install")
        sys.exit(1)

def analyze_matrix_data():
    """Simulates and visualizes Matrix data using NumPy, Pandas, and Matplotlib."""
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    # Generate 1000 data points using NumPy (as required)
    data_points = 1000
    print(f"Processing {data_points} data points...")
    
    matrix_values = np.random.randn(data_points)
    df = pd.DataFrame(matrix_values, columns=['Signal Strength'])

    # Simple visualization
    plt.figure(figsize=(10, 6))
    plt.plot(df['Signal Strength'], color='green', alpha=0.7)
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Data Point Index")
    plt.ylabel("Value")
    
    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")

if __name__ == "__main__":
    check_dependencies()
    analyze_matrix_data()

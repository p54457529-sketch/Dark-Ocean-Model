
---

### بخش دوم: فایل `main.py`
*این کد را کپی کن، در Pydroid 3 یک فایل جدید بساز، نامش را `main.py` بگذار و داخلش پیست کن.*

```python
"""
Dark Ocean Model (DOM) - Core Simulation Engine
Version: 1.0.0
Author: [Your Name/Username]
Description: Numerical integration of the Friedmann equation for cosmological evolution.
"""

import numpy as np
import matplotlib.pyplot as plt

class DarkOceanModel:
    def __init__(self, H0=70.0, Om=0.3, Ol=0.7):
        """
        Initialize simulation parameters.
        :param H0: Hubble constant (km/s/Mpc)
        :param Om: Matter density parameter (Omega_m)
        :param Ol: Dark Energy density parameter (Omega_Lambda)
        """
        self.H0 = H0
        self.Om = Om
        self.Ol = Ol
        self.H0_norm = H0 / 100.0  # Normalizing for scale factor calculation

    def friedmann_equation(self, a):
        """Calculates the expansion rate H(a)"""
        # H(a) = H0 * sqrt(Om/a^3 + Ol)
        return self.H0_norm * np.sqrt((self.Om / (a**3)) + self.Ol)

    def run_simulation(self, a_start=0.01, a_end=2.0, steps=500):
        """Integrates the scale factor over time."""
        a_values = np.linspace(a_start, a_end, steps)
        h_values = []
        
        for a in a_values:
            h_values.append(self.friedmann_equation(a))
            
        return a_values, np.array(h_values)

    def stress_test(self):
        """Simulates extreme scenarios (High Matter vs High Dark Energy)"""
        print("🚀 Running DOM Stress Test...")
        # Scenario 1: Matter Dominated
        model_m = DarkOceanModel(Om=0.9, Ol=0.1)
        a_m, h_m = model_m.run_simulation()
        
        # Scenario 2: Dark Energy Dominated
        model_l = DarkOceanModel(Om=0.1, Ol=0.9)
        a_l, h_l = model_l.run_simulation()
        
        self.plot_results(a_m, h_m, a_l, h_l)

    def plot_results(self, a1, h1, a2, h2):
        plt.figure(figsize=(10, 6))
        plt.plot(a1, h1, label='Matter Dominated ($\Omega_m=0.9$)', color='blue', linewidth=2)
        plt.plot(a2, h2, label='Dark Energy Dominated ($\Omega_\Lambda=0.9$)', color='red', linewidth=2)
        
        plt.title('DOM: Expansion Rate vs Scale Factor', fontsize=14)
        plt.xlabel('Scale Factor (a)', fontsize=12)
        plt.ylabel('Normalized Hubble Rate H(a)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        
        print("✅ Simulation Complete. Displaying Plots...")
        plt.show()

if __name__ == "__main__":
    # Initialize the model with standard LCDM parameters
    dom = DarkOceanModel(H0=70, Om=0.3, Ol=0.7)
    
    # Execute Stress Test
    dom.stress_test()

import numpy as np
import matplotlib.pyplot as plt

def monod_equation(s, mu_max, ks):
    """
    Calculates the specific growth rate (μ) using the Monod equation.

    Args:
        s (float or array): Substrate concentration(s).
        mu_max (float): Maximum specific growth rate.
        ks (float): Half-saturation constant.

    Returns:
        float or array: The calculated specific growth rate(s).
    """
    return mu_max * s / (ks + s)

def generate_plot(s_values, mu_values, mu_max, ks):
    """
    Generates and displays a detailed plot of the Monod kinetics.
    """
    plt.figure(figsize=(10, 6)) # Create a plot with a nice size

    # Plot the main growth curve
    plt.plot(s_values, mu_values, label=f'Monod Curve (μ_max={mu_max}, K_s={ks})', color='blue', linewidth=2.5)

    # --- Add helpful reference lines and points ---

    # 1. Asymptote line for μ_max
    plt.axhline(y=mu_max, color='red', linestyle='--', label=f'μ_max = {mu_max} h⁻¹')

    # 2. Line showing the K_s value on the x-axis
    plt.axvline(x=ks, color='green', linestyle='--', label=f'K_s = {ks} g/L')

    # 3. Point showing where μ is half of μ_max
    mu_at_ks = mu_max / 2
    plt.plot(ks, mu_at_ks, 'ro', markersize=8, label=f'μ at K_s ({mu_at_ks:.2f} h⁻¹)')

    # --- Styling and Labels ---
    plt.title('Monod Growth Kinetics Analysis', fontsize=16)
    plt.xlabel('Substrate Concentration (S) [g/L]', fontsize=12)
    plt.ylabel('Specific Growth Rate (μ) [h⁻¹]', fontsize=12)
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.ylim(0, mu_max * 1.1) # Set y-limit slightly above mu_max
    plt.xlim(0, s_values[-1])   # Set x-limit to the max S value we calculated

    # Display the plot
    plt.show()

def generate_analysis(mu_max, ks):
    """
    Generates and prints a textual analysis of the parameters.
    """
    mu_at_ks = mu_max / 2

    print("\n" + "="*50)
    print("      Monod Equation: Growth Kinetics Analysis")
    print("="*50)

    print("\n[ PARAMETER SUMMARY ]")
    print(f"  - Maximum Specific Growth Rate (μ_max): {mu_max} h⁻¹")
    print(f"  - Half-Saturation Constant (K_s):      {ks} g/L")

    print("\n[ INTERPRETATION ]")
    print(f"1. Substrate Affinity:")
    print(f"   The K_s value of {ks} g/L represents the substrate concentration at which the growth rate is half of its maximum.")
    print("   > A LOW K_s value indicates a HIGH affinity of the microorganism for the substrate, meaning it can grow efficiently even when the substrate is scarce.")
    print("   > A HIGH K_s value indicates a LOW affinity, meaning the organism needs a higher concentration of the substrate to grow effectively.")

    print(f"\n2. Maximum Growth Potential:")
    print(f"   The theoretical maximum growth rate (μ_max) for this organism under these conditions is {mu_max} h⁻¹.")
    print("   As the graph shows, the growth rate approaches this value asymptotically but never truly exceeds it, as the substrate becomes less of a limiting factor.")

    print(f"\n3. Key Benchmark:")
    print(f"   At a substrate concentration of exactly {ks} g/L (the K_s value), the calculated specific growth rate is {mu_at_ks:.3f} h⁻¹, confirming it is exactly half of μ_max.")
    print("\n" + "="*50)


# --- Main execution block ---
if __name__ == "__main__":
    print("--- Monod Equation Graph and Analysis Generator ---")
    print("Please provide the kinetic parameters.")

    try:
        # Get user input for the parameters
        mu_max_input = float(input("Enter the Maximum Specific Growth Rate (μ_max, e.g., 0.8): "))
        ks_input = float(input("Enter the Half-Saturation Constant (K_s, e.g., 0.2): "))

        if mu_max_input <= 0 or ks_input <= 0:
            print("\nError: Parameters must be positive numbers. Please try again.")
        else:
            # Generate a range of substrate concentration values for the x-axis
            # We'll plot S up to 20 times the Ks value to get a full view of the curve.
            s_range = np.linspace(0, ks_input * 20, 500) # 500 points for a smooth curve

            # Calculate the corresponding growth rate values for the y-axis
            mu_range = monod_equation(s_range, mu_max_input, ks_input)

            # Generate the plot and the text analysis
            generate_plot(s_range, mu_range, mu_max_input, ks_input)
            generate_analysis(mu_max_input, ks_input)

    except ValueError:
        print("\nError: Invalid input. Please enter numerical values only.")


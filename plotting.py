# plotting.py
import matplotlib.pyplot as plt

def plot_market_simulation(price_history, quantity_history):
    """
    Function to plot the price and quantity history over time.

    Parameters:
    price_history (list): List of prices over the periods.
    quantity_history (list): List of quantities over the periods.
    """
    plt.figure(figsize=(10, 5))

    # Plot Price History
    plt.subplot(1, 2, 1)
    plt.plot(price_history, marker='o')
    plt.title('Price Over Time')
    plt.xlabel('Period')
    plt.ylabel('Price')
    plt.grid(True)

    # Plot Quantity History
    plt.subplot(1, 2, 2)
    plt.plot(quantity_history, marker='o', color='orange')
    plt.title('Quantity Exchanged Over Time')
    plt.xlabel('Period')
    plt.ylabel('Quantity')
    plt.grid(True)

    # Show the plots
    plt.tight_layout()
    plt.show()

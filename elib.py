import random

from plotting import plot_market_simulation

# The simulate_market function models a simple microeconomic market scenario over a given number of periods.
# It simulates how the price and quantity of a good evolve over time based on supply and demand dynamics.

# Key Microeconomic Concepts Demonstrated:
# 1. **Demand**: The quantity of a good that consumers are willing and able to purchase at various prices.
#    - In this model, the quantity demanded is influenced by the price of the good and consumers' income.
#    - The quantity demanded decreases as the price increases, which is consistent with the Law of Demand.

# 2. **Supply**: The quantity of a good that producers are willing and able to sell at various prices.
#    - The quantity supplied is influenced by the price of the good and the producers' production costs.
#    - The quantity supplied increases as the price increases, consistent with the Law of Supply.

# 3. **Market Equilibrium**: The point where the quantity demanded by consumers equals the quantity supplied by producers.
#    - In a competitive market, the price adjusts to bring the market toward equilibrium, where supply equals demand.
#    - This simulation adjusts the price in each period based on whether there is excess demand (shortage) or excess supply (surplus).

# How the Simulation Works:
# - The function starts with an initial price and simulates the market for a specified number of periods.
# - For each period:
#     1. It calculates the quantity demanded (Qd) based on the current price and consumer income.
#     2. It calculates the quantity supplied (Qs) based on the current price and production costs.
#     3. It compares Qd and Qs to determine if there is a surplus (Qs > Qd) or a shortage (Qd > Qs).
#     4. The price is then adjusted:
#        - If there is a shortage (Qd > Qs), the price is increased to reduce demand and increase supply.
#        - If there is a surplus (Qs > Qd), the price is decreased to increase demand and reduce supply.
#     5. The current price and quantity (the lesser of Qd and Qs) are stored in history lists for plotting.

# What We Are Demonstrating:
# - This simulation demonstrates how a market self-regulates through price adjustments in response to supply and demand imbalances.
# - It shows how the market approaches equilibrium over time, where the price stabilizes, and the quantity demanded equals the quantity supplied.
# - By plotting the price and quantity over time, we can visualize these adjustments and understand the dynamics of a competitive market.
# - This model can be extended to incorporate more complex factors, such as elasticity, taxes, or subsidies, to explore more advanced economic scenarios.

# Demand and Supply functions
def quantity_demanded(price, income, price_elasticity=1.0, subsidy=0, tax=0):
    # Modify demand with elasticity, subsidy, and tax, plus random fluctuation
    effective_price = price + tax - subsidy
    base_demand = 100 - price_elasticity * (2 * effective_price) + 0.5 * income
    random_fluctuation = random.uniform(-5, 5)  # Randomly adjust demand by ±5 units
    return base_demand + random_fluctuation


def quantity_supplied(price, production_cost, price_elasticity=1.0, subsidy=0, tax=0):
    # Modify supply with elasticity, subsidy, and tax, plus random fluctuation
    effective_price = price + subsidy - tax
    base_supply = price_elasticity * (3 * effective_price) - 0.5 * production_cost
    random_fluctuation = random.uniform(-5, 5)  # Randomly adjust supply by ±5 units
    return base_supply + random_fluctuation


# Finding the equilibrium
# Market Equilibrium occurs when the quantity demanded by consumers equals the quantity supplied by producers.
# At this point, the market price stabilizes, and there is no pressure for the price to change.
# The equilibrium price is the price at which the quantity of the good demanded equals the quantity supplied.
# The equilibrium quantity is the quantity bought and sold at the equilibrium price.

def find_equilibrium(income, production_cost):
    for price in range(1, 51):  # Check prices from 1 to 50
        Qd = quantity_demanded(price, income)
        Qs = quantity_supplied(price, production_cost)
        if Qd == Qs:
            return price, Qd  # Equilibrium price and quantity

def simulate_market(income, production_cost, periods=20):
    price = 20  # Start with an initial price
    price_history = []
    quantity_history = []
    
    for period in range(periods):
        Qd = quantity_demanded(price, income)
        Qs = quantity_supplied(price, production_cost)
        
        # Store the current price and the lesser of Qd or Qs (quantity exchanged)
        price_history.append(price)
        quantity_history.append(min(Qd, Qs))
        
        # Adjust the price based on excess demand or supply
        if Qd > Qs:
            price += 1  # Increase price if demand exceeds supply
        elif Qd < Qs:
            price -= 1  # Decrease price if supply exceeds demand
        
        print(f"Period {period + 1}: Price = {price}, Quantity = {min(Qd, Qs)}")
    
    return price_history, quantity_history

# Simulate the market and get the data
price_history, quantity_history = simulate_market(income=50, production_cost=20, periods=25)

# Plot the price history
plot_market_simulation(price_history, quantity_history)
from plotting import plot_market_simulation

# Demand: The quantity of a good or service that consumers are willing to buy at various prices.
# Supply: The quantity of a good or service that producers are willing to sell at various prices.
# Law of Demand: As price decreases, quantity demanded increases (and vice versa).
# Law of Supply: As price increases, quantity supplied increases (and vice versa).
# The interaction of supply and demand determines the market price and quantity.


# Demand and Supply functions
def quantity_demanded(price, income, price_elasticity=1.0):
    return 100 - price_elasticity * (2 * price) + 0.5 * income

def quantity_supplied(price, production_cost, price_elasticity=1.0):
    return price_elasticity * (3 * price) - 0.5 * production_cost


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

def simulate_market(income, production_cost, periods=10):
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
price_history, quantity_history = simulate_market(income=50, production_cost=20, periods=15)

# Plot the price history
plot_market_simulation(price_history, quantity_history)

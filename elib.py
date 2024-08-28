# Demand: The quantity of a good or service that consumers are willing to buy at various prices.
# Supply: The quantity of a good or service that producers are willing to sell at various prices.
# Law of Demand: As price decreases, quantity demanded increases (and vice versa).
# Law of Supply: As price increases, quantity supplied increases (and vice versa).
# The interaction of supply and demand determines the market price and quantity.


# Demand and Supply functions
def quantity_demanded(price, income):
    return 100 - 2 * price + 0.5 * income

def quantity_supplied(price, production_cost):
    return 3 * price - 0.5 * production_cost

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

# Calculate the equilibrium
equilibrium_price, equilibrium_quantity = find_equilibrium(income=50, production_cost=20)

# Display the results
print(f"Equilibrium Price: {equilibrium_price}")
print(f"Equilibrium Quantity: {equilibrium_quantity}")


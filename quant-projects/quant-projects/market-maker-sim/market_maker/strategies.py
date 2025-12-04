# Placeholder for multiple strategies
def inventory_based(mid, inventory, k=0.1):
    spread = 0.02 + k*abs(inventory)
    return mid - spread/2, mid + spread/2

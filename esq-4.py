costs = []

for i in range(0, 100):
    item_cost = int(input(f"Enter the cost of item {i+1}>>>"))
    costs.append(item_cost)

total_cost = sum(costs)
avg_cost = total_cost / len(costs)
most_expensive_cost = max(costs)
least_expensive_cost = min(costs)

print("The total cost is:", total_cost)
print("The average cost is:", avg_cost)
print("The most expensive item is:", most_expensive_cost)
print("The least expensive item is:", least_expensive_cost)

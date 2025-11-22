# ---------------------------------------------------------
# Project: Analyzing Customer Orders Using Python
# ---------------------------------------------------------

# 1. STORE CUSTOMER ORDERS

# List of customer names
customers = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

# List of order details as tuples: (customer, product, price, category)
orders = [
    ("Alice", "Laptop", 899, "Electronics"),
    ("Alice", "Mouse", 25, "Electronics"),
    ("alice", "Sweatshirt", 59, "Clothing"),
    ("Bob", "T-Shirt", 20, "Clothing"),
    ("Bob", "Jeans", 45, "Clothing"),
    ("Charlie", "Vacuum Cleaner", 120, "Home Essentials"),
    ("Charlie", "Blender", 60, "Home Essentials"),
    ("Diana", "Smartphone", 699, "Electronics"),
    ("Ethan", "Coffee Maker", 80, "Home Essentials"),
    ("Ethan", "Headphones", 120, "Electronics"),
]

# Dictionary mapping each customer to a list of ordered products
customer_orders = {}
for customer, product, price, category in orders:
    customer_orders.setdefault(customer, []).append(
        {"product": product, "price": price, "category": category}
    )

# 2. CLASSIFY PRODUCTS BY CATEGORY

# Dictionary mapping product names to their categories      
product_category_map = {
    order[1]: order[3] for order in orders
}

# Set of all unique categories
unique_categories = {order[3] for order in orders}

print("\n--- Available Product Categories ---")
print(unique_categories)

# 3. ANALYZE CUSTOMER ORDERS

customer_total_spending = {}
customer_classification = {}

for customer, items in customer_orders.items():
    total = sum(item["price"] for item in items)
    customer_total_spending[customer] = total

    # Classification logic
    if total > 100:
        category = "High-value Buyer"
    elif 50 <= total <= 100:
        category = "Moderate Buyer"
    else:
        category = "Low-value Buyer"

    customer_classification[customer] = category

# 4. GENERATE BUSINESS INSIGHTS

# Revenue per category
revenue_by_category = {}

for _, product, price, category in orders:
    revenue_by_category[category] = revenue_by_category.get(category, 0) + price

# Unique products
unique_products = {order[1] for order in orders}

# List comprehension → customers who purchased Electronics
electronics_customers = [
    customer for customer, items in customer_orders.items()
    if any(item["category"] == "Electronics" for item in items)
]

# Top 3 highest spenders
top_three = sorted(
    customer_total_spending.items(), key=lambda x: x[1], reverse=True
)[:3]

# 5. ORGANIZE AND DISPLAY DATA

print("\n--- Customer Spending Summary ---")
for customer in customers:
    print(f"{customer}: ${customer_total_spending[customer]} ({customer_classification[customer]})")

# Customers who purchased from multiple categories
customer_categories = {customer: {item["category"] for item in items}
                       for customer, items in customer_orders.items()}

multi_category_customers = [c for c, cats in customer_categories.items() if len(cats) > 1]

# Customers who bought both Electronics and Clothing
electronics_buyers = {c for c, cats in customer_categories.items() if "Electronics" in cats}
clothing_buyers = {c for c, cats in customer_categories.items() if "Clothing" in cats}

both_electronics_clothing = electronics_buyers & clothing_buyers

# Display Insights

print("\n--- Revenue by Category ---")
for cat, rev in revenue_by_category.items():
    print(f"{cat}: ${rev}")

print("\n--- Unique Products ---")
print(unique_products)

print("\n--- Customers Who Purchased Electronics ---")
print(electronics_customers)

print("\n--- Top 3 Highest Spending Customers ---")
for c, amt in top_three:
    print(f"{c}: ${amt}")

print("\n--- Customers Buying from Multiple Categories ---")
print(multi_category_customers)

print("\n--- Customers Who Bought Both Electronics and Clothing ---")
print(both_electronics_clothing)

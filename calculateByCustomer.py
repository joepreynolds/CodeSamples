from typing import List, Dict

def calculate_total_spent(orders: List[Dict[str,  str | int | float]]) -> Dict[int, float]:
    total_spent_by_customer = {}
    for order in orders:
        customer_id = order["customer_id"]
        total_amount = order["total_amount"]
        print(customer_id)

        if customer_id in total_spent_by_customer:
            total_spent_by_customer[customer_id] += total_amount
        else:
            total_spent_by_customer[customer_id] = total_amount

    return total_spent_by_customer

orders = [
    {"order_id": 1, "customer_id": 101, "order_date": "2024-01-01", "total_amount": 50.20},
    {"order_id": 2, "customer_id": 102, "order_date": "2024-01-02", "total_amount": 30.50},
    {"order_id": 3, "customer_id": 101, "order_date": "2024-01-03", "total_amount": 25.30},
    {"order_id": 4, "customer_id": 103, "order_date": "2024-01-04", "total_amount": 40.10},
]
result = calculate_total_spent(orders)
print(result)

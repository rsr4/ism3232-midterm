orders = [
    {"company": "Pine Books", "seat_price": 40.00, "seats": 5, "education": False},
    {"company": "Quarry School", "seat_price": 35.00, "seats": 12, "education": True},
    {"company": "Redwood Cargo", "seat_price": 45.00, "seats": 60, "education": False},
    {"company": "Summit College", "seat_price": 50.00, "seats": 150, "education": True},
    {"company": "Tidal Health", "seat_price": 55.00, "seats": 100, "education": False},
    {"company": "Upland Farms", "seat_price": 60.00, "seats": 24, "education": False},
    {"company": "Vega Dental", "seat_price": 30.00, "seats": 25, "education": True},
    {"company": "Willow Law", "seat_price": 400.00, "seats": 9, "education": False},
]

from business_rules import *

print("Cloudstep Software - Order Report")

for order in orders:
    license_total = calculate_license_total(
        order["seat_price"], order["seats"], order["education"]
    )
    needs_review = needs_contract_review(license_total)
    trainer = get_trainer(order["seats"], license_total)

    print(format_license_line(order["company"], license_total, needs_review, trainer))

print(f"Orders: {len(orders)}")
print(f"Total Licensed: ${total_licensed(orders):.2f}")
print(f"Average License: ${total_licensed(orders) / len(orders):.2f}")
print(f"Largest License total: {largest_license(orders)}")
total_reviews = 0
for order in orders:
    license_total = calculate_license_total(
        order["seat_price"], order["seats"], order["education"]
    )
    needs_review = needs_contract_review(license_total)

    if needs_review == True:
        total_reviews += 1

print(f"Contract reviews needed: {total_reviews}")
total_trainer = 0
for order in orders:
    license_total = calculate_license_total(
        order["seat_price"], order["seats"], order["education"]
    )
    trainer_need = get_trainer(order["seats"], license_total)

    if trainer_need == True:
        total_trainer += 1

print(f"Trainers assigned: {total_trainer}")

# Cloudstep Software Business functions


def calculate_license_cost(seat_price: float, seats: int) -> float:
    subtotal = seat_price * seats
    return subtotal


def get_seat_discount(seats: int, education: bool = False) -> float:
    if seats >= 50 and education == True:
        return 0.16
    elif seats >= 10:
        return 0.07
    else:
        return 0.0


def calculate_license_total(
    seat_price: float, seats: int, education: bool = False
) -> float:
    discounted_total = calculate_license_cost(seat_price, seats) * (
        1 - get_seat_discount(seats, education)
    )

    if discounted_total <= 400:
        return discounted_total + 60
    else:
        return discounted_total


def needs_contract_review(total: float) -> bool:
    if total > 5000:
        return True
    else:
        return False


def get_trainer(seats: int, total: float) -> bool:
    if seats >= 25 or total > 3000:
        return True
    else:
        return False


def total_licensed(orders: list) -> float:
    total = 0
    for order in orders:
        license_total = calculate_license_total(
            order["seat_price"], order["seats"], order["education"]
        )

        total += license_total

    return total


def largest_license(orders: list) -> str:
    largest_total = 0
    largest_company = ""

    for order in orders:
        license_total = calculate_license_total(
            order["seat_price"], order["seats"], order["education"]
        )
        if license_total > largest_total:
            largest_total = license_total
            largest_company = order["company"]

    return largest_company


def format_license_line(
    company: str, total: float, contract_review: bool, trainer: bool
) -> str:
    if contract_review == True:
        review_text = "yes"
    else:
        review_text = "no"

    if trainer == True:
        trainer_text = "yes"
    else:
        trainer_text = "no"

    return f"{company}: ${total:,.2f} | Contract Review: {review_text} | Trainer: {trainer_text}"

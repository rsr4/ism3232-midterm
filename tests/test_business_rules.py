# tests for business rule functions
from business_rules import *


def test_calculate_license_cost():
    license_cost = calculate_license_cost(40.00, 5)
    assert license_cost == 200.00


def test_get_seat_discount_education():
    discount = get_seat_discount(51, True)
    assert discount == 0.16


def test_get_seat_discount_seat_under():
    discount = get_seat_discount(49, True)
    assert discount == 0.07


def test_get_seat_discount_over():
    discount = get_seat_discount(10)
    assert discount == 0.07


def test_get_seat_discount_under():
    discount = get_seat_discount(9)
    assert discount == 0.0


def test_calculate_license_total_over():
    license_total = calculate_license_total(400.00, 9, True)
    assert license_total == 3600


def test_calculate_license_total_boundary_under():
    license_total = calculate_license_total(100.00, 4)
    assert license_total == 460.00


def test_calculate_license_total_boundary_over():
    license_total = calculate_license_total(80.20, 5)
    assert license_total == 401.00


def test_calculate_license_total_under_with_discount():
    license_total = calculate_license_total(26.73, 15, True)
    assert license_total == 432.88349999999997


def test_calculate_license_total_under():
    license_total = calculate_license_total(50.00, 5)
    assert license_total == 310


def test_needs_contract_review_over():
    contract = needs_contract_review(6000.00)
    assert contract == True


def test_needs_contract_review_under():
    contract = needs_contract_review(4000.00)
    assert contract == False


def test_needs_contract_review_boundary_over():
    contract = needs_contract_review(5001.00)
    assert contract == True


def test_needs_contract_review_boundary_under():
    contract = needs_contract_review(5000.00)
    assert contract == False


def test_get_trainer_true():
    trainer = get_trainer(25, 3001.00)
    assert trainer == True


def test_get_trainer_false():
    trainer = get_trainer(20, 2000.00)
    assert trainer == False


def test_get_trainer_true_seat():
    trainer = get_trainer(30, 1000.00)
    assert trainer == True


def test_get_trainer_true_price():
    trainer = get_trainer(20, 5000.00)
    assert trainer == True


def test_get_trainer_false_boundary():
    trainer = get_trainer(24, 3000.00)
    assert trainer == False


def test_total_licensed():
    test_orders = [
        {"company": "Apple", "seat_price": 100.00, "seats": 50, "education": True},
        {"company": "Microsoft", "seat_price": 40.00, "seats": 50, "education": False},
    ]

    test = total_licensed(test_orders)
    assert test == 6060


def test_largest_license_tie():
    test_orders = [
        {"company": "Apple", "seat_price": 100.00, "seats": 50, "education": False},
        {"company": "Microsoft", "seat_price": 100.00, "seats": 50, "education": False},
    ]

    test = largest_license(test_orders)
    assert test == "Apple"


def test_largest_license_empty():
    test_orders = []

    test = largest_license(test_orders)
    assert test == ""


def test_format_license_line():
    license_line = format_license_line("Apple", 5000.00, True, True)

    assert license_line == "Apple: $5,000.00 | Contract Review: yes | Trainer: yes"


def test_format_license_line_false():
    license_line = format_license_line("Apple", 5000.00, False, False)

    assert license_line == "Apple: $5,000.00 | Contract Review: no | Trainer: no"

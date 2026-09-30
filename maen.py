from pyscript import document


def create_order(event=None):
    # Item names and prices
    items = {
        "item1": ("Mountain Dew", 110),
        "item2": ("Coca-cola", 120),
        "item3": ("Doritos", 80),
        "item4": ("Egg Sandwich", 150),
        "item5": ("John", 1)
    }

    receipt = ""
    total = 0

    # Check which items were selected
    for item_id, (name, price) in items.items():
        checkbox = document.querySelector(f"#{item_id}")

        if checkbox.checked:
            receipt += f"{name:<20} ₱{price:>6.2f}<br>"
            total += price

    # If nothing was selected
    if total == 0:
        document.querySelector("#output1").innerHTML = (
            "Please select at least one item."
        )
        return

    # Display total
    receipt += "<br>"
    receipt += f"<strong>{'TOTAL':<20} ₱{total:>6.2f}</strong>"

    # Put receipt into the HTML
    document.querySelector("#output1").innerHTML = receipt

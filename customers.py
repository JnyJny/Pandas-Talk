"""
"""

from faker import Faker
from faker.providers import misc, date_time


class Provider(misc.Provider, date_time.Provider):
    def order_number(self) -> str:
        return self.numerify("##-####")

    def order_date(self) -> str:
        return self.date_this_month()

    def ship_date(self) -> str:
        if self.random_int(min=0, max=1):
            return self.future_date()
        return "0"

    def inventory_number(self) -> str:
        return self.bothify("??##-??#").upper()

    def unit_price(self) -> float:
        return self.numerify("@##.##")

    def units(self) -> int:
        return self.random_int(min=1, max=10)


def csv_data(n_customers: int = 10) -> str:
    fake = Faker()
    fake.add_provider(Provider)
    headers = [
        "Order Number",
        "Order Date",
        "Inventory Number",
        "Unit Price",
        "Units",
        "Ship Date",
        "Name",
        "Address",
        "Email",
        "Phone Number",
        "Date of Birth",
    ]

    columns = [f'{{{{{h.casefold().replace(" ", "_")}}}}}' for h in headers]

    return fake.csv(header=headers, data_columns=columns, num_rows=n_customers)

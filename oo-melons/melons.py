"""Classes for melon orders."""


class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    order_type = None
    tax = 0
    species = None
    qty = 0

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = 0

        if self.species == "Christmas":
            total = (1 + self.tax) * self.qty * (base_price * 1.5)
            print(total)
        else:
            total = (1 + self.tax) * self.qty * base_price

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = 0

    #     if self.species == "Christmas":
    #         base_price *= 1.5
    #     elif self.qty < 10:
    #         total = 3 + (1 + self.tax) * self.qty * base_price

    #     else:
    #         total = (1 + self.tax) * self.qty * base_price

    #     return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

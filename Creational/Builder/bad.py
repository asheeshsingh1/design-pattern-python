from typing import List, Optional

# Represents a customizable Burger Meal
class BurgerMeal:
    def __init__(self,
            bun_type: str,
            patty: str,
            sides: Optional[str] = None,
            toppings: Optional[List[str]] = None,
            cheese: bool = False,
            drink: Optional[str] = None
        ):
        
        # Mandatory components
        self.bun_type = bun_type
        self.patty = patty

        # Optional components
        self.sides = sides
        self.toppings = toppings
        self.cheese = cheese
        self.drink = drink

    def to_string(self) -> str:
        return (
            f"Bun: {self.bun_type}\nPatty: {self.patty}\nCheese: {self.cheese}\nDrink: {self.drink}\nSides: {self.sides}\nDrink: {self.drink}")

def main():
    # Keyword arguments help readability in Python
    plain_burger = BurgerMeal(bun_type="wheat", patty="veg")
    print(plain_burger.to_string())

if __name__ == "__main__":
    main()
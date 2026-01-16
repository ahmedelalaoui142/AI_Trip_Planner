class Calculator:
    @staticmethod
    def multiply(a: int, b: int) -> int:
        """Multiply two integers"""
        return a * b
    @staticmethod
    def calculate_total(*x: float) -> float:
        """Calculate the total of a list of numbers"""
        return sum(x)
    @staticmethod
    def calculate_daily_budget(total: float, days :int) -> float:
        """Calculate the daily budget"""
        return total / days if days > 0 else 0
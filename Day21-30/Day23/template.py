# Custom Exception
class InvalidAmountError(Exception):
    pass

def process_transaction(balance, amount):
    try:
        # Risky code
        print("Starting transaction...")

        # ValueError example
        amount = int(amount)

        # Custom exception
        if amount < 0:
            raise InvalidAmountError("Amount cannot be negative")

        # ZeroDivisionError example
        result = balance / amount

    except ValueError as e:
        print("Value Error:", e)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

    except InvalidAmountError as e:
        print("Custom Error:", e)

    except Exception as e:
        # Handles any unexpected exception
        print("Unexpected Error:", e)

    else:
        # Runs only if NO exception occurs
        print("Transaction successful")
        print("Result:", result)
        return result

    finally:
        # Always executes
        print("Cleaning up resources...")
        print("Transaction completed\n")


# Function calls
process_transaction(100, "10")     # No error
process_transaction(100, "0")      # ZeroDivisionError
process_transaction(100, "-5")     # Custom exception
process_transaction(100, "abc")    # ValueError

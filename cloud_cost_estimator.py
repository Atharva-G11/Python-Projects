"""A beginner-friendly, illustrative monthly cloud-cost estimator.

The prices are examples entered by the user; verify current provider pricing before
making any spending decision.
"""

from decimal import Decimal, InvalidOperation


def read_non_negative(prompt: str) -> Decimal:
    """Read a non-negative decimal value from the terminal."""
    while True:
        try:
            value = Decimal(input(prompt).strip())
            if value < 0:
                raise ValueError
            return value
        except (InvalidOperation, ValueError):
            print("Please enter a non-negative number.")


def main() -> None:
    print("Monthly Cloud Cost Estimator")
    print("Enter your expected usage and the price shown by your cloud provider.\n")

    compute_hours = read_non_negative("Compute hours per month: ")
    compute_rate = read_non_negative("Compute price per hour: $")
    storage_gb = read_non_negative("Storage in GB: ")
    storage_rate = read_non_negative("Storage price per GB-month: $")
    egress_gb = read_non_negative("Data transfer out in GB: ")
    egress_rate = read_non_negative("Data transfer price per GB: $")

    compute_cost = compute_hours * compute_rate
    storage_cost = storage_gb * storage_rate
    egress_cost = egress_gb * egress_rate
    total = compute_cost + storage_cost + egress_cost

    print("\nEstimated monthly cost")
    print(f"  Compute:       ${compute_cost:.2f}")
    print(f"  Storage:       ${storage_cost:.2f}")
    print(f"  Data transfer: ${egress_cost:.2f}")
    print("  " + "-" * 25)
    print(f"  Total:         ${total:.2f}")
    print("\nThis is an estimate, not a provider quote.")


if __name__ == "__main__":
    main()

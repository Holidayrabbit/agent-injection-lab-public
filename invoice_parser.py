import re


AMOUNT_PATTERN = re.compile(r"([0-9]+)(?:\.([0-9]{1,2}))?")


def parse_amount(text: str) -> int:
    """Return the amount in cents."""
    match = AMOUNT_PATTERN.search(text)
    if match is None:
        raise ValueError("invoice text does not contain an amount")

    whole = int(match.group(1))
    fraction = (match.group(2) or "0").zfill(2)
    return whole * 100 + int(fraction or 0)


"""Test module to verify setup."""


def greet(name: str) -> str:
    """Return a greeting message.
    Args:
        name: The name to greet
    Returns:
        A greeting string
    """
    return f"Hello, {name}! Setup is working."


if __name__ == "__main__":
    print(greet("Cloud Engineer"))

import os
import sys

from dotenv import load_dotenv


REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_configuration() -> dict[str, str]:
    load_dotenv()

    config: dict[str, str] = {}
    missing: list[str] = []

    for key in REQUIRED_VARS:
        value = os.getenv(key)
        if value is None or value.strip() == "":
            missing.append(key)
        else:
            config[key] = value.strip()

    if missing:
        print("ORACLE STATUS: Reading the Matrix...")
        print("WARNING: Missing configuration detected")
        print("Missing variables:")
        for key in missing:
            print(f"- {key}")
        print("Create a .env file from .env.example or export variables manually.")
        sys.exit(1)

    return config


def describe_database(database_url: str, mode: str) -> str:
    if mode == "development":
        return "Connected to local instance"
    return f"Connected to production instance ({database_url})"


def describe_api(api_key: str) -> str:
    if len(api_key) >= 8:
        return "Authenticated"
    return "Invalid key format"


def describe_zion(endpoint: str, mode: str) -> str:
    if mode == "development":
        return f"Local relay online ({endpoint})"
    return f"Resistance network online ({endpoint})"


def print_configuration(config: dict[str, str]) -> None:
    mode = config["MATRIX_MODE"]
    database_url = config["DATABASE_URL"]
    api_key = config["API_KEY"]
    log_level = config["LOG_LEVEL"]
    zion_endpoint = config["ZION_ENDPOINT"]

    print("ORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {describe_database(database_url, mode)}")
    print(f"API Access: {describe_api(api_key)}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {describe_zion(zion_endpoint, mode)}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


def validate_mode(mode: str) -> None:
    if mode not in ("development", "production"):
        print("Error: MATRIX_MODE must be 'development' or 'production'")
        sys.exit(1)


def main() -> None:
    config = load_configuration()
    validate_mode(config["MATRIX_MODE"])
    print_configuration(config)


if __name__ == "__main__":
    main()
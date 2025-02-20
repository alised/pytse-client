"""
This is a test file to ensure all symbols in symbols_name.json file are
downloadable.
This process takes a long time so it's not part of the unit test
"""

from pytse_client import all_symbols, download, download_client_types_records

if __name__ == "__main__":
    download("وبملت")
    download_client_types_records("وبملت")

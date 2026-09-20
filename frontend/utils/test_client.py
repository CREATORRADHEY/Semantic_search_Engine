"""
Manual API smoke test.

Run manually:

python frontend/utils/test_client.py
"""

from frontend.utils.api_client import api


def main():

    print(api.health())


if __name__ == "__main__":

    main()
#!/usr/bin/env python3
"""
requests_instagram_recovery.py

Simple script to trigger Instagram’s account-recovery SMS/email flow via their
web API. It fetches a fresh CSRF token, computes the required jazoest header,
and sends the password-reset request.

Usage:
    python requests_instagram_recovery.py <username_or_email>
"""

import sys
import requests


def send_recovery_request(username: str) -> None:
    """
    Send a password-reset request to Instagram for the given username.

    This will cause Instagram to send an SMS or email with a recovery link
    to the contact point on record for that account.

    :param username: Instagram username, or email
    """
    session = requests.Session()
    # Prime the session to get a fresh csrftoken cookie
    session.get("https://www.instagram.com/")
    csrf_token = session.cookies.get("csrftoken")
    if not csrf_token:
        raise RuntimeError("Unable to obtain csrftoken from instagram.com")

    # Instagram’s jazoest header is '2' + sum of each character code in csrftoken
    jazoest = "2" + str(sum(ord(ch) for ch in csrf_token))

    # Mirror the headers Instagram’s JS would send
    session.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/135.0.0.0 Safari/537.36"
        ),
        "X-CSRFToken": csrf_token,
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/password/reset/",
        "Origin": "https://www.instagram.com",
    })

    payload = {
        "email_or_username": username,
        "jazoest": jazoest,
    }

    response = session.post(
        "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/",
        data=payload,
    )

    print(f"Status: {response.status_code}")
    try:
        data = response.json()
        print(data)
    except ValueError:
        print("Non-JSON response:", response.text)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python main.py <username_or_email>")
        sys.exit(1)

    user = sys.argv[1]
    try:
        send_recovery_request(user)
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
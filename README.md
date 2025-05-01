# Instagram Password Reset Trigger 🔑

This is a simple Python script to trigger Instagram's account recovery process via their public web API.  
It sends a password reset link to the account's registered email or phone number.

## 🚀 Features

- Automatically fetches CSRF token.
- Calculates required headers (`jazoest`) as expected by Instagram.
- Sends recovery link request.
- Prints out the API response (useful for debugging).

## 📌 Usage

### Install dependencies

```bash
pip install requests
```

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

### Run the Script

```bash
python main.py <username_or_email_or_phone>
```
 
#### Example

```bash
python mainpy johndoe
```
This will cause Instagram to send a recovery email or SMS to the account.

## ⚡ Notes

- This script is for educational and personal account recovery purposes only.
- Do not use this on accounts you do not own. It may violate Instagram's Terms of Service and/or privacy laws.
- There are no rate limits or advanced error handling — use responsibly.

## 📜 License
MIT License

## 🙏 Disclaimer
This tool is provided for educational purposes only; using it to harass or target others may be illegal and/or violate Instagram's Terms of Service. The author is not responsible for any misuse.

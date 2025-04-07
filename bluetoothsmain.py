import webbrowser
import urllib.parse

def open_whatsapp_chat(phone_number: str, message: str):
    # Format the message properly for a URL
    encoded_message = urllib.parse.quote(message)

    # Create the wa.me URL
    wa_url = f"https://wa.me/{phone_number}?text={encoded_message}"

    # Open the URL in the default browser
    webbrowser.open(wa_url)
    print(f"Opening WhatsApp chat with {phone_number}...")

# Example usage
if __name__ == "__main__":
    phone = "919360871557"  # Use full number with country code, no + or spaces
    msg = "Hi there! 👋 This message is sent using wa.me and Python."
    open_whatsapp_chat(phone, msg)

import webbrowser
import urllib.parse

def open_whatsapp_chat(phone_number: str, message: str):
    """
    Opens a WhatsApp chat with a specific phone number and prefilled message.

    Parameters:
    - phone_number (str): The phone number in international format (no '+' or spaces).
    - message (str): The message to prefill.
    """

    # Encode the message for URL
    encoded_message = urllib.parse.quote(message)

    # Create the WhatsApp link
    url = f"https://wa.me/{phone_number}?text={encoded_message}"

    # Open it in the default browser (on phone or PC)
    webbrowser.open(url)
    print(f"Opening WhatsApp chat with {phone_number}...")

# Example usage
if __name__ == "__main__":
    phone = "919360871557"  # Replace with actual number in international format
    message = "Hey! Just checking in from my Python script 🐍"
    open_whatsapp_chat(phone, message)

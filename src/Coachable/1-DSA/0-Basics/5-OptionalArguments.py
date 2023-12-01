"""
Optional Arguments
"""


def send_email(to: str, subject: str, message: str, cc: str = None, bcc: str = None):
    print("To:", to)
    print("Subject:", subject)
    print("Message:", message)
    if cc:
        print("CC:", cc)
    if bcc:
        print("BCC:", bcc)


# Call the function with only required arguments
send_email("john.doe@example.com", "Hello", "How are you?")
# Output:
# To: john.doe@example.com
# Subject: Hello
# Message: How are you?

# Call the function with optional arguments
send_email("jane.doe@example.com", "Greetings", "I hope you are doing well.", "info@example.com", "secret@example.com")
# Output:
# To: jane.doe@example.com
# Subject: Greetings
# Message: I hope you are doing well.
# CC: info@example.com
# BCC: secret@example.com

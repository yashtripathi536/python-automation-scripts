# Email Extractor - CodeAlpha Task 3 (Task Automation)
import re

INPUT_FILE = "input.txt"
OUTPUT_FILE = "emails.txt"

# Regex pattern for an email address
EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def read_file(filename):
    """Read the text file and return its content. Return None if there is a problem."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Create it in the same folder as this script.")
    except Exception as e:
        print(f"Error while reading the file: {e}")
    return None


def extract_emails(text):
    """Find all emails in the text and return a sorted list without duplicates."""
    emails = re.findall(EMAIL_PATTERN, text)
    unique_emails = sorted(set(email.lower() for email in emails))
    return unique_emails


def save_emails(emails, filename):
    """Write emails to a file, one per line."""
    with open(filename, "w", encoding="utf-8") as file:
        for email in emails:
            file.write(email + "\n")


def main():
    print("=== Email Extractor ===")

    text = read_file(INPUT_FILE)
    if text is None:
        return

    emails = extract_emails(text)

    if not emails:
        print("No email addresses found in the file.")
        return

    save_emails(emails, OUTPUT_FILE)

    print(f"\nFound {len(emails)} unique email(s):")
    for email in emails:
        print(f"  - {email}")
    print(f"\nSaved to '{OUTPUT_FILE}'")


main()
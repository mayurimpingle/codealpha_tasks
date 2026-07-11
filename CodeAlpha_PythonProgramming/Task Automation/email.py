import re

# Input file (contains text with emails)
input_file = r"C:\PROJECTS\CodeAlpha_PythonProgramming\Task Automation\emails.txt"

# Output file (where extracted emails will be saved)
output_file = r"C:\PROJECTS\CodeAlpha_PythonProgramming\Task Automation\extracted_emails.txt"

# Read the input file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Regex pattern to match email addresses
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Find all emails
emails = re.findall(pattern, text)

# Save emails to output file
with open(output_file, "w", encoding="utf-8") as f:
    for email in emails:
        f.write(email + "\n")

print("Emails extracted and saved to extracted_emails.txt")
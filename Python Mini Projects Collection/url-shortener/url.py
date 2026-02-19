import json
import random
import string

FILE_NAME = "urls.json"

# Load existing URLs
def load_urls():
    try:
        with open(FILE_NAME, "r") as f:
            data = f.read().strip()
            if not data:   # file is empty
                return {}
            return json.loads(data)
    except FileNotFoundError:
        return {}

# Save URLs
def save_urls(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Generate short code
def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def shorten_url(long_url):
    urls = load_urls()
    short_code = generate_short_url()
    urls[short_code] = long_url
    save_urls(urls)
    return short_code

def retrieve_url(short_code):
    urls = load_urls()
    return urls.get(short_code, "URL not found")

# Main Program
while True:
    print("\n1. Shorten URL\n2. Retrieve URL\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        long_url = input("Enter long URL: ")
        short = shorten_url(long_url)
        print(f"Short URL: http://short.ly/{short}")

    elif choice == "2":
        code = input("Enter short code: ")
        print("Original URL:", retrieve_url(code))

    elif choice == "3":
        break
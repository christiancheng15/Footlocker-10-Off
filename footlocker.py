import requests
import uuid

# Initialize a session to persist cookies and settings across requests
s = requests.Session()

# Headers to be used in requests
headers = {
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.footlocker.com.au/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

# Proxy configuration (replace with your actual proxies)
proxy_dict = {
    "http": "xxxxxxxxxx",
    "https": "xxxxxxxxxx",
}

# Function to generate a promotional code from Footlocker
def generate_code():
    try:
        # Make a GET request to the promotional code endpoint with headers and proxies
        r = s.get(url=f"https://site.bluecore.com/fetchpromo?ns=footlocker_au&cid=52051f4f-b717-4e52-82c3-49504c9ca55e&distinct_id={uuid.uuid4()}", headers=headers, proxies=proxy_dict)
        
        # Raise HTTPError for bad responses
        r.raise_for_status()
        
        # Extract and return the code from the JSON response
        return r.json()["code"]
    except (requests.RequestException, KeyError) as e:
        # Handle exceptions if request fails or JSON parsing error occurs
        print(f"Error generating code: {e}")
        return None

# Function to save generated code to a file
def save_to_file(code):
    with open("footlocker_codes.txt", "a") as file:
        file.write(f"{code}\n")

# Main execution block
if __name__ == "__main__":
    try:
        # Prompt user for the quantity of codes to generate
        quantity = int(input("Quantity: "))
        
        # Validate user input
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        # Counter for generated codes
        generated_count = 0
        
        # Loop until desired quantity of codes is generated
        while generated_count < quantity:
            # Generate a promotional code
            code = generate_code()
            
            # Check if code is valid (contains "10OFF" substring)
            if code and "10OFF" in code:
                # Save valid code to file
                save_to_file(code)
                print(f"Generated code: {code}")
                generated_count += 1
            else:
                print("Failed to generate valid code.")
    
    # Handle specific exceptions
    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
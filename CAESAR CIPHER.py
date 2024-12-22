def encrypt(text, s):
    result = ""

    for char in text:
        if char.isupper(): 
            result += chr((ord(char) - 65 + s) % 26 + 65)  
        elif char.islower():  
            result += chr((ord(char) - 97 + s) % 26 + 97)  
        else:
            result += char   
    return result

def main():
    print("Welcome to the Caesar Cipher Program!")
    
    
    text = input("Enter the text you want to encrypt: ")
    
    while True:
        try:
            s = int(input("Enter the shift value (1-25): "))
            if 1 <= s <= 25:
                break
            else:
                print("Please enter a shift value between 1 and 25.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 25.")
    
    encrypted_text = encrypt(text, s)
    
    print("\nEncryption Complete!")
    print(f"Original Text: {text}")
    print(f"Shift Value: {s}")
    print(f"Encrypted Text: {encrypted_text}")

if __name__ == "__main__":
    main()

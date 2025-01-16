def display_menu():
    print("1. Enter encryption/decryption key")
    print("2. Encrypt a message")
    print("3. Decrypt a message")
    print("4. Exit")

class EncryptDecrypt:
    def __init__(self):
        self.__encr_decr_key = None

    @property
    def encr_decr_key(self):
        if self.__encr_decr_key is None:
            raise ValueError("Encryption/Decryption key has not been set")
        return self.__encr_decr_key

    @encr_decr_key.setter
    def encr_decr_key(self, value):
        if not 1 <= value <= 26:
            raise ValueError("Encryption/Decryption key must be between 1 and 26")
        self.__encr_decr_key = value

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            if char == " ":
                encrypted_message += " "
            else:
                encrypted_message += chr((ord(char) - 97 + self.encr_decr_key) % 26 + 97)
        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = ""
        for char in encrypted_message:
            if char == " ":
                decrypted_message += " "
            else:
                decrypted_message += chr((ord(char) - 97 - self.encr_decr_key) % 26 + 97)
        return decrypted_message

def main():
    encrypt_decrypt = EncryptDecrypt()
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            try:
                key = int(input("Enter encryption/decryption key: "))
                encrypt_decrypt.encr_decr_key = key
            except ValueError as e:
                print(e)
        elif choice == "2":
            try:
                message = input("Enter a message to encrypt: ")
                print("Encrypted message:", encrypt_decrypt.encrypt(message))
            except ValueError as e:
                print(e)
        elif choice == "3":
            try:
                encrypted_message = input("Enter an encrypted message to decrypt: ")
                print("Decrypted message:", encrypt_decrypt.decrypt(encrypted_message))
            except ValueError as e:
                print(e)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
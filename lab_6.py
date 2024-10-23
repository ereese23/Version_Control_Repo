# Elijah Reese Lab 6 Group 94 Partner: Ata Saka
def encode(key):
   encoded_password = ""
   for char in key:
       if char.isdigit():
           new_digit = (int(char) + 3) % 10
           encoded_password += str(new_digit)
       else:
           raise ValueError("Password must contain 8 digits.")
   return encoded_password

def decode(encoded_key):
   decoded_password = ""
   for char in encoded_key:
       if char.isdigit():
           new_digit = (int(char) - 3) % 10
           decoded_password += str(new_digit)
   return decoded_password

def main():
   encoded_password = None
   decoded_password = None


   while True:
       print("Menu")
       print("-------------")
       print("1. Encode")
       print("2. Decode")
       print("3. Quit")
       choice = input("Please enter an option: ")


       if choice == '1':
           decoded_password = input("Please enter your password to encode: ")
           if len(decoded_password) == 8 and decoded_password.isdigit():
               encoded_password = encode(decoded_password)
               print("Your password has been encoded and stored!")
           else:
               print("Invalid input. Please enter an 8-digit password.")


       elif choice == '2':
           if encoded_password is not None:
               print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
           else:
               print("No password has been encoded.")


       elif choice == '3':
           break


       else:
           print("Invalid choice.")


if __name__ == "__main__":
   main()

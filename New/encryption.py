# We implemented a common encrpytion technique called as " Vigenère cipher "
# We used internet to learn about this encryption technique.

class Encryption:
    
    encryption_key = "PythonMidSemProject"


    #This method takes a normal string and returs an encrypted string.
    @staticmethod
    def encrypt(plaintext):
        encrypted_text = []
        key = Encryption.encryption_key
        key_length = len(key)
        key_indices = [ord(char.upper()) - 65 for char in key]
        key_index = 0
        
        for char in plaintext:
            if char.isalpha():
                shift = key_indices[key_index % key_length]
                key_index += 1
                
                if char.islower():
                    encrypted_text.append(chr((ord(char) - 97 + shift) % 26 + 97))
                else:
                    encrypted_text.append(chr((ord(char) - 65 + shift) % 26 + 65))
            else:
                encrypted_text.append(char)

        return ''.join(encrypted_text)



    
    #This method takes an encrypted string and returs an un-encrypted string.
    @staticmethod
    def decrypt(ciphertext):
        decrypted_text = []
        key = Encryption.encryption_key
        key_length = len(key)
        key_indices = [ord(char.upper()) - 65 for char in key]
        key_index = 0
        
        for char in ciphertext:
            if char.isalpha():
                shift = key_indices[key_index % key_length]
                key_index += 1
                
                if char.islower():
                    decrypted_text.append(chr((ord(char) - 97 - shift) % 26 + 97))
                else:
                    decrypted_text.append(chr((ord(char) - 65 - shift) % 26 + 65))
            else:
                decrypted_text.append(char)  
        
        return ''.join(decrypted_text)


# if __name__ =="__main__":
#     message = "AryanSharma0205@124bk"
#     encrypted_message = Encryption.encrypt(message)
#     decrypted_message = Encryption.decrypt(encrypted_message)

#     print(f"Original: {message}")
#     print(f"Encrypted: {encrypted_message}")
#     print(f"Decrypted: {decrypted_message}")

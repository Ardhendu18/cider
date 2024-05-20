Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):
    cipher_text=" "
    for char in text:
        if char in Alphabet:
           position=Alphabet.index(char)
           new_position=(position+shift_key)%26
           cipher_text += Alphabet[new_position]
        else:
           cipher_text += char   
    print(f"Here is the text after encryption: {cipher_text}")

def decryption(cipher_text,shift_key):
    plain_text=" "
    for char in text:
        if char in Alphabet:
           position=Alphabet.index(char)
           new_position=(position-shift_key)%26
           plain_text += Alphabet[new_position]
        else:
           plain_text += char   
    print(f"Here is the text after decryption: {plain_text}")

flag=False
while not flag:
    what_to_do=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
    text=input("Type your message:\n").lower()
    shift=int(input("Enter shift key:\n"))
    if what_to_do=="encrypt":
      encryption(text,shift)
    elif what_to_do=="decrypt":
      decryption(text,shift)
    run_again=input("Type 'yes' to continue, type 'no' to exit.\n")
    if run_again=='no':
       flag=True
       print("Caesar Cipher projrct is completed")  

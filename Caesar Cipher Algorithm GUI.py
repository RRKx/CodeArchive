from tkinter import *

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt():
    global lowercase_letters, uppercase_letters, plaintext_entry, key_entry, encrypted_text_label

    try:
        plaintext = plaintext_entry.get()
        key = int(key_entry.get())

        ciphertext = ""

        for character in plaintext:
            if character in lowercase_letters:
                letter_index = lowercase_letters.index(character)
                
                new_index = (letter_index + key) % 26
                ciphertext += lowercase_letters[new_index]

            elif character in uppercase_letters:
                letter_index = uppercase_letters.index(character)
                
                new_index = (letter_index + key) % 26
                ciphertext += uppercase_letters[new_index]
            else:
                ciphertext += character
        
        encrypted_text_label.config(text=f"Encrypted: {ciphertext}")
    except UnboundLocalError and ValueError as error:
        encrypted_text_label.config(text="Encrypted text: INVALID KEY")

def decrypt():
    global lowercase_letters, uppercase_letters, ciphertext_entry, key_entry, decrypted_text_label
    
    try:
        ciphertext = ciphertext_entry.get()
        key = int(key_entry.get())

        plaintext = ""
        
        for character in ciphertext:
            if character in lowercase_letters:
                letter_index = lowercase_letters.index(character)
                
                new_index = (letter_index - key) % 26
                plaintext += lowercase_letters[new_index]

            elif character in uppercase_letters:
                letter_index = uppercase_letters.index(character)
                
                new_index = (letter_index - key) % 26
                plaintext += uppercase_letters[new_index]
            else:
                plaintext += character

        decrypted_text_label.config(text=f"Decrypted: {plaintext}")
    
    except UnboundLocalError and ValueError as error:
        decrypted_text_label.config(text="Decrypted text: INVALID KEY")


window = Tk()

window.title("Caesar Cipher Algorithm")
window.geometry("300x300")
window.resizable(False, False)

text_label1 = Label(window, text="______________Key______________")
text_label1.grid(row=1, sticky=W)

key_entry = Entry(window, width=33)
key_entry.grid(row=2, column=0, ipadx=5, ipady=5, sticky=W)

empty_label1 = Label(window, width=35)
empty_label1.grid(row=3, sticky=W)

text_label2 = Label(window, text="______________Plaintext______________")
text_label2.grid(row=4, sticky=W)

plaintext_entry = Entry(window, width=33)
plaintext_entry.grid(row=5, column=0, ipadx=5, ipady=5, sticky=W)

encrypted_text_label = Label(window, text="Encrypted text: N/A")
encrypted_text_label.grid(row=6, column=0, sticky=W)

encrypt_button = Button(window, text="Encrypt", command=encrypt)
encrypt_button.grid(row=7, sticky=W)

empty_label2 = Label(window, width=35)
empty_label2.grid(row=3, sticky=W)

text_label3 = Label(window, text="______________Ciphertext______________")
text_label3.grid(row=9, sticky=W)

ciphertext_entry = Entry(window, width=33)
ciphertext_entry.grid(row=10, column=0, ipadx=5, ipady=5, sticky=W)

decrypted_text_label = Label(window, text="Decrypted text: N/A")
decrypted_text_label.grid(row=11, column=0, sticky=W)

decrypt_button = Button(window, text="Decrypt", command=decrypt)
decrypt_button.grid(row=12, sticky=W)

empty_label3 = Label(window, width=35)
empty_label3.grid(row=13, sticky=W)

window.mainloop()

# Used ChatGPT for wrap behavior

# Notes to self
# (letter_index + key) % 26 is used for wrap behavior
# You can use bracket notation on a string to access specific characters

# Code is not perfect but it works (to an extent)
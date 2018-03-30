import random
from itertools import starmap, cycle


class substitution_cipher(object):
  """ Substitution cipher class to encrypt and
  decrypt plain and cipher text respectively"""

  def __init__(self):
    self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_alphabet = list(self.alphabet.upper())
    random.shuffle(random_alphabet)
    self.key = 'HKJXUBFSONMYTECZWPLDAVIQRG'
    self.plain_text_file = 'train_plain.txt'
    self.cipher_text_file = 'train_cipher.txt'
    with open(self.plain_text_file, "r") as plain_text:
      self.plain_text_data = plain_text.read()
    with open(self.cipher_text_file, "r") as cipher_text:
      self.cipher_text_data = cipher_text.readlines()
      self.cipher_text_data = self.cipher_text_data[0]

  def encrypt(self):
    """For encryption substitute the value of plain text character by corresponding key"""
    # key map is a dictionary mapping the alphabet to it's substitued key
    keyMap = dict(zip(self.alphabet, self.key))
    message = ''
    for c in self.plain_text_data:
      if c == ' ':
        message = message + ' '
      else:
        if keyMap.get(c) is not None:
          message = message + keyMap.get(c)
    return message

  def decrypt(self):
    """For decryption substitute the key by it's corresponding plain text character"""
    # key map is a dictionary mapping the key to the alphabet for decryption
    keyMap = dict(zip(self.key, self.alphabet))
    message = ''
    for c in self.cipher_text_data:
      if c == ' ':
        message = message + ' '
      else:
        if keyMap.get(c) is not None:
          message = message + keyMap.get(c)
    return message

  def generate_data(self):
    gdata = open(self.cipher_text_file, 'w')
    cipher = self.encrypt()
    gdata.write(cipher)


class vigenere_cipher(object):
  """ Vigenere cipher class to encrypt and
  decrypt plain and cipher text respectively"""

  def __init__(self):
    self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
    self.key = 'KEY'
    self.plain_text_file = 'train_plain.txt'
    self.cipher_text_file = 'train_cipher.txt'
    with open(self.plain_text_file, "r") as plain_text:
      self.plain_text_data = plain_text.read()
    with open(self.cipher_text_file, "r") as cipher_text:
      self.cipher_text_data = cipher_text.read()

  def encrypt(self):
    """ Cipher text = (position of alphabet in plain text + position + key) % 26 """
    key_length = len(self.key)
    key_as_int = [ord(i) for i in self.key]
    plaintext_int = []
    for c in self.plain_text_data:
      if c == ' ':
        plaintext_int.append(-1)
      else:
        plaintext_int.append(ord(c))
    ciphertext = ''
    for i in range(len(plaintext_int)):
      if plaintext_int[i] == -1:
        ciphertext += ' '
      else:
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext

  def decrypt(self):
    """ Cipher text = (position of alphabet in plain text - position + key) % 26 """
    key_length = len(self.key)
    key_as_int = [ord(i) for i in self.key]
    ciphertext_int = []
    for c in self.cipher_text_data:
      if c == ' ':
        ciphertext_int.append(-1)
      else:
        ciphertext_int.append(ord(c))
    plaintext = ''
    for i in range(len(ciphertext_int)):
      if ciphertext_int[i] == -1:
        plaintext += ' '
      else:
        value = (ciphertext_int[i] + key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext

  def generate_data(self):
    gdata = open(self.cipher_text_file, 'a')
    gdata.write('\n')
    cipher = self.encrypt()
    gdata.write(cipher)


if __name__ == "__main__":
  substitution_cipher = substitution_cipher()
  vigenere_cipher = vigenere_cipher()
  substitution_cipher.generate_data()
  vigenere_cipher.generate_data()

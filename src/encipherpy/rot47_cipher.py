from _string_number_convert import _stringToAscii as stringToAscii
from _string_number_convert import _asciiToString as asciiToString

def rot47(plainText):
  asciiNumbers = stringToAscii(plainText)
  cipherNumbers = []

  for number in asciiNumbers:
    shiftedNumber = number + 47
    shiftedNumber = shiftedNumber % 126
    if shiftedNumber < 33:
      shiftedNumber = shiftedNumber + 32
    cipherNumbers.append(shiftedNumber)

  cipherText = asciiToString(cipherNumbers)
  print(asciiNumbers)
  print(cipherNumbers)
  return cipherText
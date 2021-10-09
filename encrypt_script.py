"""
encrypt based on bitwise "exclusive or"

Reference:
https://www.youtube.com/watch?v=HHlInKhVz3s


structure:

main
command line interface
calls every other function
keyboard read - filename : string, key : int (1-255)

read_file
arguments - filename : string
returns - contents : bytearray

crypt
arguments - contents : bytearray, key : int
returns - en(de)crypted : bytearray

write_encrypted
arguments - contents : bytearray, filename : string
write to file - en(de)crypted content

"""


import os


def read_file(file_):

    with open(file_, "rb") as file_object:
        text = file_object.read()

    return bytearray(text)


def write_encrypted(contents_, filename_):

    with open(filename_, "wb") as file_enc:
        file_enc.write(contents_)


def crypt(text_bytes_, key_):

    for index, value in enumerate(text_bytes_):
        text_bytes_[index] = value ^ key_

    return text_bytes_


def main():

    # command line interface

    print("___directory contents___")
    for file_ in os.listdir():
        print(file_)
    print("________________________")

    original_filename = input("file to encrypt: ")
    key = int(input("key (in range 1-255): "))
    encrypted_file = "cc-" + original_filename

    contents = read_file(original_filename)

    write_encrypted(crypt(contents, key), encrypted_file)


# main call

main()

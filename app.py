from time import sleep as sleep
import os
from PIL import Image
from colorama import Fore, Style, init

init(autoreset=True)

HEADER_LENGTH = 256  # Define the header length

def display_banner():
    banner = Fore.WHITE + """
###################################################################################################
##                                                                                               ##
##  ######## #### ##       ########     #######     #### ##     ##    ###     ######   ########  ##
##  ##        ##  ##       ##          ##     ##     ##  ###   ###   ## ##   ##    ##  ##        ##
##  ##        ##  ##       ##                 ##     ##  #### ####  ##   ##  ##        ##        ##
##  ######    ##  ##       ######       #######      ##  ## ### ## ##     ## ##   #### ######    ##
##  ##        ##  ##       ##          ##            ##  ##     ## ######### ##    ##  ##        ##
##  ##        ##  ##       ##          ##            ##  ##     ## ##     ## ##    ##  ##        ##
##  ##       #### ######## ########    #########    #### ##     ## ##     ##  ######   ########  ##
##                                                                                               ##
###################################################################################################
    """ + Fore.GREEN + """
    Made by""" + Fore.LIGHTBLUE_EX + " D4RKH0R1Z0N " + Fore.WHITE + "(" + Fore.BLUE + "https://github.com/D4RKH0R1Z0N" + Fore.WHITE + ")" + "\n" + Fore.LIGHTBLUE_EX + "    Discord " + Fore.YELLOW + "and " + Fore.LIGHTMAGENTA_EX + "Instagram " + Fore.WHITE + ": @D4RKH0R1Z0N\n"
    print(banner)

def file_to_image(input_file, output_image="output.png"):
	print(Style.RESET_ALL + """
       ###################################
       ##                               ##
       ##""" + Fore.BLUE + """  Converting... Please Wait... """ + Style.RESET_ALL + """##
       ##                               ##
       ###################################

Meanwhile Follow me on my Socials!\n""" + Fore.GREEN + """
    Made by""" + Fore.LIGHTBLUE_EX + " D4RKH0R1Z0N " + Fore.WHITE + "(" + Fore.BLUE + "https://github.com/D4RKH0R1Z0N" + Fore.WHITE + ")" + "\n" + Fore.LIGHTBLUE_EX + "    Discord " + Fore.YELLOW + "and " + Fore.LIGHTMAGENTA_EX + "Instagram " + Fore.WHITE + ": @D4RKH0R1Z0N\n")
    try:
        with open(input_file, 'rb') as f:
            file_data = f.read()

        # Create a header containing the original filename
        header = os.path.basename(input_file).encode() + b'\x00' * (HEADER_LENGTH - len(os.path.basename(input_file)))
        header_data = header + file_data

        # Create an image with the header + file data
        image = Image.new('L', (len(header_data), 1))
        image.putdata(header_data)

        # Save the image
        image.save(output_image)
        sleep(1.8)
        print(Fore.GREEN + f"File '{input_file}' has been converted and saved as '{output_image}'" + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.RED + "Error: Input file not found." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)
        print("")

def image_to_file(input_image):
	print(Style.RESET_ALL + """
       ###################################
       ##                               ##
       ##""" + Fore.BLUE + """  Converting... Please Wait... """ + Style.RESET_ALL + """##
       ##                               ##
       ###################################

Meanwhile Follow me on my Socials!\n""" + Fore.GREEN + """
    Made by""" + Fore.LIGHTBLUE_EX + " D4RKH0R1Z0N " + Fore.WHITE + "(" + Fore.BLUE + "https://github.com/D4RKH0R1Z0N" + Fore.WHITE + ")" + "\n" + Fore.LIGHTBLUE_EX + "    Discord " + Fore.YELLOW + "and " + Fore.LIGHTMAGENTA_EX + "Instagram " + Fore.WHITE + ": @D4RKH0R1Z0N\n")
    try:
        # Open the image
        image = Image.open(input_image)

        # Get the image data
        image_data = list(image.getdata())

        # Extract the header (containing the original filename)
        header = bytes(image_data[:HEADER_LENGTH]).rstrip(b'\x00')

        # Extract the original filename from the header
        original_filename = header.decode()
        sleep(1.8)

        if original_filename:
            # Extract the file data (excluding the header)
            file_data = bytes(image_data[HEADER_LENGTH:])

            # Save the file with the extracted original file name
            with open(original_filename, 'wb') as f:
                f.write(file_data)

            print(Fore.GREEN + f"Image '{input_image}' has been converted back to '{original_filename}'" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Error: Original filename not found in the header." + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.RED + "Error: Input image not found." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)

def main():
    display_banner()

    while True:
        print(Fore.CYAN + "Select a option -" + Style.RESET_ALL)
        print("")
        print(Fore.LIGHTBLUE_EX + "1> " + Fore.WHITE + "Convert File to Image")
        print(Fore.LIGHTBLUE_EX + "2> " + Fore.WHITE + "Convert Image back to File")
        print(Fore.LIGHTBLUE_EX + "CLS> " + Fore.WHITE + "Clears the Screen")
        print(Fore.LIGHTBLUE_EX + "CREDITS> " + Fore.WHITE + "Displays Credits")
        print(Fore.LIGHTBLUE_EX + "ABOUT> " + Fore.WHITE + "Displays project Information")
        print(Fore.RED + "EXIT> " + Fore.WHITE + "Exit" + Style.RESET_ALL)
        print("")

        option = input(">>> ")

        if option == "1":
            input_file = input(Fore.CYAN + "Enter the path to the file you want to convert: " + Style.RESET_ALL)
            file_to_image(input_file)
        elif option == "2":
            input_image = input(Fore.CYAN + "Enter the path to the image you want to convert back: " + Style.RESET_ALL)
            image_to_file(input_image)
        elif option.lower() == "cls":
            print(chr(27) + "[2J")
            print(chr(27) + "[2J")
            display_banner()
        elif option.lower() == "credits":
            print(Fore.GREEN + """
    Made by""" + Fore.LIGHTBLUE_EX + " D4RKH0R1Z0N " + Fore.WHITE + "(" + Fore.BLUE + "https://github.com/D4RKH0R1Z0N" + Fore.WHITE + ")" + " and " + Fore.LIGHTBLUE_EX + "D4RKH0R1Z0N " + Fore.WHITE + "(" + Fore.BLUE + "https://github.com/D4RKH0R1Z0N" + Fore.WHITE + ")" + Fore.BLUE + " ONLY\n")
            print("""Socials -\n""" + """
    GitHub""" + Fore.LIGHTBLUE_EX + " @D4RKH0R1Z0N " + "\n" + Fore.LIGHTBLUE_EX + "    Discord " + Fore.YELLOW + "and " + Fore.LIGHTMAGENTA_EX + "Instagram " + Fore.WHITE + ": @D4RKH0R1Z0N\n")
        elif option.lower() == "about":
            print("""
Project Name: "File2Image - Your Universal File Conversion Tool"

Description:
File2Image is a versatile and efficient open-source GitHub project that empowers you to seamlessly convert any file into an image file and effortlessly revert it back to its original format. Whether you're looking to preserve your data, enhance your file sharing capabilities, or even optimize your storage, File2Image has you covered.

Key Features:
- Universal File Conversion: Convert virtually any file type, from documents to multimedia files, into image format and vice versa.

- Data Compression: Reduce file size without compromising quality, making it ideal for optimizing storage or accelerating data transfer.

- Intuitive User Interface: An easy-to-use interface ensures that anyone can harness the power of File2Image with minimal effort.

- File Integrity: Maintain file integrity throughout the conversion process, ensuring your data remains intact.

- Customizable Options: Fine-tune compression settings and image output parameters to suit your specific needs.

- Open Source: Built with transparency in mind, File2Image is open source, making it customizable and adaptable to your unique requirements.

Unlock the potential of your files with File2Image today. Whether you're a developer seeking a powerful tool or an everyday user looking for a simple yet effective way to manage your files, File2Image is your all-in-one solution. Download it now and join the growing community of users who are transforming their file management experience.
""")
        elif option.lower() == "exit":
            break
        else:
            print(Fore.RED + "Error: Invalid option. Please choose a valid option." + Style.RESET_ALL)

if __name__ == "__main__":
    main()

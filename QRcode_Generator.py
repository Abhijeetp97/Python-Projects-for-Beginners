import qrcode
from PIL import Image

def generate_qr_code(data, filename, fill_color='black', back_color='white'):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code instance with custom colors
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # Save the image
    img.save(filename)
    print(f"QR code saved as {filename}")

def main():
    print("Welcome to the QR Code Generator!")
    
    # Choose the color for the QR code
    fill_color = input("Enter the color for the QR code (e.g., 'black', 'blue', 'red'): ").strip()
    back_color = input("Enter the background color for the QR code (e.g., 'white', 'yellow'): ").strip()
    
    # Get multiple inputs from the user
    user_inputs = input("Enter the text or URLs to generate QR codes (separated by commas): ").strip().split(',')
    user_inputs = [x.strip() for x in user_inputs]  # Remove any leading/trailing whitespace
    
    # Get filenames from the user
    filenames = input("Enter the filenames for each QR code (separated by commas): ").strip().split(',')
    filenames = [x.strip() for x in filenames]  # Remove any leading/trailing whitespace

    if len(user_inputs) != len(filenames):
        print("Error: The number of texts/URLs and filenames must be equal.")
        return

    for data, filename in zip(user_inputs, filenames):
        generate_qr_code(data, filename, fill_color, back_color)

    print("All QR codes have been generated successfully!")

if __name__ == "__main__":
    main()
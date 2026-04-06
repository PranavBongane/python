import qrcode as qr
# def generateQR(qr_str):
#     img = qr.make(qr_str)
#     img.save(f"{qr_str[:10]}_QR.png")

def generateQR(qr_str):   
    qr_img = qr.QRCode(
    version = 1,  # Size: 1 (21x21) to 40 (177x177)
    error_correction = qr.constants.ERROR_CORRECT_H, # High (30% recovery)
    box_size = 10, # Pixels per box
    border = 4,    # Minimum border width
)
    qr_img.add_data(qr_str)
    qr_img.make(fit = True)
    img = qr_img.make_image(fill_color = "black", back_color = "white")
    img.save(f"{qr_str[:10]}_QR.png")

def main():
    qr_str = input("Enter link to generate Qr-code: ").strip()
    if not qr_str:
        print("Please enter valid input ❌")
        return
    
    try:
        generateQR(qr_str)
        print("QR Code generated successfully ✅")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__" :
    main()
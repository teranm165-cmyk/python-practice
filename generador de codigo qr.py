while True:

 import qrcode

 data = input("escibe tu url o texto para generar el QR")
 nombre_archivo = input("como quieres que se llame el archivo (sin ectensiones):")
 qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5)

 qr.add_data(data) 
 qr.make(fit=True)

 ing = qr .make_image(fill_color = "black" , black_color = "white" )

 ing .save(nombre_archivo + ".png")

 print(f" QR generado con exito! se guardo como {nombre_archivo}.png")

 generar_otro_codigo_qr = input("quieres generar otro qr (si/no):").lower()
 if generar_otro_codigo_qr == "no":
  print("gracia por usar genrador de QR")
 break
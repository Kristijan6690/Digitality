from PIL import Image
import io
import requests
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"P:\Programs\Tesseract\tesseract.exe"

def scan_image(image_path):
    #Slika se dohvaca sa storega pa ju dohvacamo preko requesta
    response = requests.get(image_path)

    #Otvaramo sliku koja je proslijedena preko path-a
    img = Image.open(io.BytesIO(response.content))

    #Pomocu tesseracta analiziramo sliku te pronadeni tekst spremamo u varijablu 'text' za daljnju obradu
    #   proslijedujemo sliku racuna te postaljamo parametre na kojem jezicima treba pronaci rijeci
    text = pytesseract.image_to_string(img, lang='hrv+bos')
    
    #Posto je gornja funkcija dosta spora, rezultate OCR-a pohranjujemo u txt file za daljne testiranje i ponovnu upotrebu
    
    print('Image scanned!\n')
    return(text)

if __name__ == "__main__":
    path = 'https://raw.githubusercontent.com/mstjepan28/Test-files/master/20200323_142140.jpg?token=ANIL4UJ2NZNBT6QFSXKGXKS62YT5Q'
    
    result = scan_image(path)
    print(result)
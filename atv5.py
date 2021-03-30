from PIL import Image, ImageOps, ImageColor
      
# creating a image1 object 
imagem_original = Image.open('imagem.jpeg') 

cor = ImageColor.getrgb("red")

imagem_contorno = ImageOps.expand(imagem_original, border = 10, fill = cor) 

imagem_contorno.save("500x500_com_borda.jpg")

imagem_contorno.show()
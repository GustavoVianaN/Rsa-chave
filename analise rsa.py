import random

import time

def function_double(a,b):

    if(a<b):

        return a

    else:
        c=a%b

        return c

def Key_start_Generate(number_escolha): 

    def minimo_multiplo_comum(note1,note2):

        sobra_rest_number = 1
        
        while(note2 != 0):

            sobra_rest_number = note1%note2

            note1 = note2

            note2 = sobra_rest_number

        return note1

    while True:

        Key_start = random.randrange(2,Gerar_algoritm_de_N) 

        if(minimo_multiplo_comum(Gerar_algoritm_de_N,Key_start) == 1):

            return Key_start

def Gerar_algoritm(algoritm): 

    if(Function_number_primo(algoritm)):

        return algoritm-1

    else:

        return False

def Function_number_primo(note): 

    if (note <= 1):

        return False

    if (note <= 3):

        return True

    if (note%2 == 0 or note%3 == 0):

        return False

    i = 5

    while(i * i <= note):

        if (note%i == 0 or note%(i+2) == 0):

           return False

        i+=6

    return True

def aleatory_random():

    while True:

        first_term=random.randrange(1,100) 

        if(Function_number_primo(first_term)==True):

            return first_term

def cipher(function_texto,Key_start,note):

    tam = len(function_texto)

    i = 0

    lista = []

    while(i < tam):

        letter = function_texto[i]

        k = ord(letter)

        k = k**Key_start

        chave_calculate = function_double(k,note)

        lista.append(chave_calculate)

        i += 1

    return lista

def Functio_Deciprapy(cifra,note,chave_calculate):

    lista = []

    i = 0

    tamanho = len(cifra)

    while i < tamanho:

        result = cifra[i]**chave_calculate

        texto = function_double(result,note)

        letra = chr(texto)

        lista.append(letra)

        i += 1

    return lista

def calculate_private_key(Gerar_algoritm_de_N,Key_start):

    chave_calculate = 0

    while(function_double(chave_calculate*Key_start,Gerar_algoritm_de_N)!=1):

        chave_calculate += 1

    return chave_calculate

def function_1024bits(public_key):

  while public_key < (9**128):

    public_key = public_key*2

  return public_key

def function_1024bits_private(private_key_chave):

  while private_key_chave <= (9**128):

    private_key_chave = private_key_chave*2

  return private_key_chave

def function_2048bits(public_key):

  while public_key <= (9**256):

    public_key = public_key*2

  return public_key

def function_2048bits_private(private_key_chave):

  while private_key_chave <= (9**256):

    private_key_chave = private_key_chave*2

  return private_key_chave

def function_4096bits(public_key):

  while public_key <= (9**512):

    public_key = public_key*2

  return public_key

def function_4096bits_private(private_key_chave):

  while private_key_chave <= (9**512):

    private_key_chave = private_key_chave*2

  return private_key_chave

def function_8192bits(public_key):

  while public_key <= (9**1024):

    public_key = public_key*2

  return public_key

def function_8192bits_private(private_key_chave):

  while private_key_chave <= (9**1024):

    private_key_chave = private_key_chave*2

  return private_key_chave

menu = ' '
while menu != '10':
  
  print("1 - a. Utilizando o algoritmo RSA com chave pública e privada de 1024 bits")
  print("2 - b. Utilizando o algoritmo RSA com chave pública e privada de 2048 bits")
  print("3 - c. Utilizando o algoritmo RSA com chave privada e privada de 4096 bits")
  print("4 - d. Utilizando o algoritmo RSA com chave privada e privada de 8192 bits")

  menu = input()

  if menu =='1':

      while menu == '1':

        text = input("Insert message: ")

        first_term = aleatory_random()

        second_term = aleatory_random() 

        note = first_term*second_term

        Gerar_first_term = Gerar_algoritm(first_term)

        Gerar_second_term = Gerar_algoritm(second_term) 

        Gerar_algoritm_de_N = Gerar_second_term*Gerar_first_term

        Key_start = Key_start_Generate(Gerar_algoritm_de_N) 

        public_key = (Key_start)

        function_1024bits(public_key)

        public_key = function_1024bits(public_key)

        print('Chave Publica  ', public_key)

        Function_text_Ciphra = cipher(text,Key_start,note)

        print('Mensagem Cifrada  ', Function_text_Ciphra)

        chave_calculate = calculate_private_key(Gerar_algoritm_de_N,Key_start)

        chave_calculate_private = function_1024bits_private(chave_calculate)

        print('Chave Privada  ', chave_calculate_private)

        Descriptography_text = Functio_Deciprapy(Function_text_Ciphra,note,chave_calculate)

        print('Mensagem Descriptografada', Descriptography_text)

        print("---")

        print("Tempo de Execução")

        print("Public Key")

        inicio = time.time()

        aleatory_random()

        aleatory_random()

        Gerar_algoritm(first_term)

        Gerar_algoritm(second_term) 

        Key_start_Generate(Gerar_algoritm_de_N) 

        (Key_start)

        function_1024bits(public_key)

        fim = time.time()

        print(fim - inicio)

        inicio = time.time()

        print("private Key")

        aleatory_random()

        aleatory_random()

        Gerar_algoritm(first_term)

        Gerar_algoritm(second_term) 

        Key_start_Generate(Gerar_algoritm_de_N) 

        (Key_start)

        Functio_Deciprapy(Function_text_Ciphra,note,chave_calculate)

        function_1024bits_private(chave_calculate)

        fim = time.time()

        print(fim - inicio)

        retorar_codigo = input("Digite 1 para criptografar novamente ou 0 para retornar ao menu: ")

        if retorar_codigo == '1':

          continue

        else:

          break

  if menu =='2':

      while menu == '2':

        text = input("Insert message: ")

        first_term = aleatory_random()

        second_term = aleatory_random() 

        note = first_term*second_term

        Gerar_first_term = Gerar_algoritm(first_term)

        Gerar_second_term = Gerar_algoritm(second_term) 

        Gerar_algoritm_de_N = Gerar_second_term*Gerar_first_term

        Key_start = Key_start_Generate(Gerar_algoritm_de_N) 

        public_key = (Key_start)

        function_2048bits(public_key)

        public_key = function_2048bits(public_key)

        print('Chave Publica  ', public_key)

        Function_text_Ciphra = cipher(text,Key_start,note)

        print('Mensagem Cifrada  ', Function_text_Ciphra)

        chave_calculate = calculate_private_key(Gerar_algoritm_de_N,Key_start)

        chave_calculate_private = function_2048bits_private(chave_calculate)

        print('Chave Privada  ', chave_calculate_private)

        Descriptography_text = Functio_Deciprapy(Function_text_Ciphra,note,chave_calculate)

        print('Mensagem Descriptografada', Descriptography_text)

        print("---")

        print("Tempo de Execução")

        print("Public Key")

        inicio = time.time()

        aleatory_random()

        aleatory_random()

        Gerar_algoritm(first_term)

        Gerar_algoritm(second_term) 

        Key_start_Generate(Gerar_algoritm_de_N) 

        (Key_start)

        function_1024bits(public_key)

        fim = time.time()

        print(fim - inicio)

        inicio = time.time()

        print("private Key")

        aleatory_random()
        
        aleatory_random()

        Gerar_algoritm(first_term)
        
        Gerar_algoritm(second_term) 

        Key_start_Generate(Gerar_algoritm_de_N) 

        (Key_start)

        Functio_Deciprapy(Function_text_Ciphra,note,chave_calculate)

        function_1024bits_private(chave_calculate)

        fim = time.time()

        print(fim - inicio)

        retorar_codigo = input("Digite 1 para criptografar novamente ou 0 para retornar ao menu: ")

        if retorar_codigo == '2':

          continue

        else:

          break

  if menu =='3':

      while menu == '3':

        text = input("Insert message: ")

        first_term = aleatory_random()

        second_term = aleatory_random() 

        note = first_term*second_term

        Gerar_first_term = Gerar_algoritm(first_term)

        Gerar_second_term = Gerar_algoritm(second_term) 

        Gerar_algoritm_de_N = Gerar_second_term*Gerar_first_term

        Key_start = Key_start_Generate(Gerar_algoritm_de_N) 

        public_key = (Key_start)

        function_4096bits(public_key)

        public_key = function_4096bits(public_key)

        print('Chave Publica  ', public_key)

        Function_text_Ciphra = cipher(text,Key_start,note)

        print('Mensagem Cifrada  ', Function_text_Ciphra)

        chave_calculate = calculate_private_key(Gerar_algoritm_de_N,Key_start)

        chave_calculate_private = function_4096bits_private(chave_calculate)

        print('Chave Privada  ', chave_calculate_private)

        Descriptography_text = Functio_Deciprapy(Function_text_Ciphra,note,chave_calculate)

        print('Mensagem Descriptografada', Descriptography_text)

        print("---")

        print("Tempo de Execução")

        print("Public Key")

        inicio = time.time()

        aleatory_random()

        aleatory_random()

        Gerar_algoritm(first_term)

        Gerar_algoritm(second_term) 

        Key_start_Generate(Gerar_algoritm_de_N) 

        (Key_start)

        function_1024bits(public_key)

        fim = time.time()

        print(fim - inicio)

        inicio = time.time()

        print("private Key")

        aleatory_random()

        aleatory_random()

        Gerar_algoritm(first_term)

        Gerar_algoritm(second_term) 

        Key_start_Generate(Gerar_algoritm_de_N) 

        (Key_start)

        Functio_Deciprapy(Function_text_Ciphra,note,chave_calculate)

        function_1024bits_private(chave_calculate)

        fim = time.time()

        print(fim - inicio)

        retorar_codigo = input("Digite 1 para criptografar novamente ou 0 para retornar ao menu: ")

        if retorar_codigo == '3':

          continue

        else:

          break

  if menu =='4':

      while menu == '4':

        text = input("Insert message: ")

        first_term = aleatory_random()

        second_term = aleatory_random() 

        note = first_term*second_term

        Gerar_first_term = Gerar_algoritm(first_term)

        Gerar_second_term = Gerar_algoritm(second_term) 

        Gerar_algoritm_de_N = Gerar_second_term*Gerar_first_term

        Key_start = Key_start_Generate(Gerar_algoritm_de_N) 

        public_key = (Key_start)

        function_8192bits(public_key)

        public_key = function_8192bits(public_key)

        print('Chave Publica  ', public_key)

        Function_text_Ciphra = cipher(text,Key_start,note)
        
        print('Mensagem Cifrada  ', Function_text_Ciphra)

        chave_calculate = calculate_private_key(Gerar_algoritm_de_N,Key_start)

        chave_calculate_private = function_8192bits_private(chave_calculate)

        print('Chave Privada  ', chave_calculate_private)

        Descriptography_text = Functio_Deciprapy(Function_text_Ciphra,note,chave_calculate)

        print('Mensagem Descriptografada', Descriptography_text)

        print("---")

        print("Tempo de Execução")

        print("Public Key")

        inicio = time.time()

        aleatory_random()

        aleatory_random()

        Gerar_algoritm(first_term)
        
        Gerar_algoritm(second_term) 

        Key_start_Generate(Gerar_algoritm_de_N) 

        (Key_start)

        function_1024bits(public_key)

        fim = time.time()

        print(fim - inicio)

        inicio = time.time()

        print("private Key")

        aleatory_random()

        aleatory_random()

        Gerar_algoritm(first_term)

        Gerar_algoritm(second_term) 

        Key_start_Generate(Gerar_algoritm_de_N) 

        (Key_start)

        Functio_Deciprapy(Function_text_Ciphra,note,chave_calculate)

        function_1024bits_private(chave_calculate)

        fim = time.time()

        print(fim - inicio)

        retorar_codigo = input("Digite 1 para criptografar novamente ou 0 para retornar ao menu: ")

        if retorar_codigo == '4':

          continue

        else:
          
          break
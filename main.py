import time, datetime
from playsound import playsound

print(" _____                     _   _                     ")
print("|_   _|                   | | (_)                    ")
print("  | | ___  _ __ ___   __ _| |_ _ _ __ ___   ___ _ __ ")
print("  | |/ _ \\| '_ ` _ \\ / _` | __| | '_ ` _ \\ / _ \\ '__|")
print("  | | (_) | | | | | | (_| | |_| | | | | | |  __/ |   ")
print("  \\_/\\___/|_| |_| |_|\\__,_|\\__|_|_| |_| |_|\\___|_|  \n\n")   
                                                     
                                                     

def countdown(timespan):
  while timespan > 0:
    timer = datetime.timedelta(seconds = timespan)
    print(timer)
    time.sleep(1)
    timespan -= 1
  playsound('ring.mp3')

print("Bem vindo ao Tomatimer, quantos ciclos você gostaria de fazer?");
cycles = int(input(":"))
print("Serão", cycles, "ciclos")

counter = 0
while counter < cycles:
  input("Aperte enter para começar o tempo de foco")
  countdown(1500)
  input("Aperte enter para começar o tempo de descanso")
  countdown(300)
  counter += 1
print("Todos os ciclos foram terminados")

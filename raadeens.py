import random
gewonnen = 0
veloren = 0
Rounds = 1   
gokteller = 10

while Rounds <= 20:

    print("Dit is ronde: " + str(Rounds) + '\n'+ 'Je hebt: ' + str(gewonnen) + ' gewonnen. ' + ' Je hebt: ' + str(veloren) + ' veloren.')
    AnotherGame = input('Wil je nog een ronde spelen |yes or no: ')
    if AnotherGame == 'yes':
         randomNummer = random.randrange(1000)

         while gokteller >= 0:
            # print(randomNummer)
             if gokteller == 0:
                print('you lose!'  ' Het getal was: ' + str(randomNummer))
                veloren = veloren + 1
                break

             guess = input('Je hebt nog: ' + str(gokteller) + ' Pogingen'+ ' Raad een nummer onder de 1000 of stop met "Q": ')
             if guess != 'Q':
                 if int(guess) == randomNummer:
                     gewonnen = gewonnen + 1
                     print('You Win!')
                     break 
             
                 else:
                  guess = int(guess)
                  howClose = randomNummer - guess
                 if howClose >= -20 and howClose <= 20:
                    print('Je bent heet')
                 elif howClose >= -50 and howClose<= 50:
                    print('Je bent warm')
                 elif guess < howClose:
                    print('Hoger')
                 elif guess > howClose:
                    print('Lager')

             else:
                 veloren = veloren + 1
                 break
        
             gokteller = gokteller - 1
    else: 
        break
    Rounds = Rounds + 1

print('Final Score!' + '\n' + ' Je hebt zoveel gewonnen: ' + str(gewonnen) + ' Je hebt zoveel veloren: ' +str(veloren))
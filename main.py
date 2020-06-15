#!/bin/python3

def showInstructions():
  #print a main menu and the commands

  print('''
**********
Welcome to   ,,,,                                      mw
     ▐▒▒▀▒▒▒                                   ]▒▒
     ▐▓▌,w▓▓` ╠█▌  ▒█M ▒█▄█▓█▄  ▄█▀▓█▓M╓█▀▀▓█m ]▓▒  ▄█▓▀██w ▒█  ▐██  ██` ██
     ▐▒▓▀▀▓█▌ ╢▒▌  ▒▒M ▒▒Ñ  ▒▒ "▓▌w@▓Ñ  µµ▄▄▒▒ ]▒▒ ╠▒▌  ]▒▒ ▐▓▌]▒▒▒▌▐▒▌  ``
     ╟▒▒,,╟▒▒ ╢▒▒,╓▒▒M ▒▒[  ▒▒ ║▒▒▒▒,  ▒▒▒ ║▒▒ ]▒▒ ]▒▒,,║▒▒  ▒▒▒▒ ▒▒▒▒   ╓m
     '╜╜╜╜╙`   ╙╚╝╙╙╝  ╙╝`  ╚╚ ╓░╜╙╙░░  ╙╝╝╙╚╜  ╝╜  `╙╚╝╜`    ╝╝┘ "╝╝`   ╚╜
                               ╙░░╢░░╜
                            Bungalow:
 
 
 
 
               ,,
      ▒▒▒▒▒▒▒▒]▒▒                   ╓@▒▒▒▒▒W
        ├▒▒   ]▒▒▄██▄   g▄██▄,     @▒▌     ` ,▄███▄, ]█▌▄██▄µ▄█▌m  ,▄██▌µ
        ├▓▒   ]▓▓` ▒▓▌ ▒▓▌µµ▓▓     ▓▓  ▒▓▓█▌  `,w▒▓▒ ]▓▓` ▒▓▌  ▓▓ ]▓▓µµ▒▓▌
        ]▒▒   ]▒▒  ▐▒▒ ▒▒▒````     ▒▒▒,  ╠▒▒ ╟▒▒`]▒▒ ]▒▒  ╢▒▌  ▒▒ ▐▒▒````
        └▒▒    ▒▒  ╙░Ñ  ╜▒░╢▒Ñ      `╜▒░░░Ñ╜ `╢░╢Ñ▒▒  ▒▒  ╢░K  ▒▒  ╙╢░╢░▒
                            The Game
========
INSTRUCTIONS:
--------------
Get to the garden with a key and a shield.
Avoid the monster!
--------------
Commands:
  go [direction]
  get [item]
========
Good Luck! ;-)
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = ['apple']

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : { 
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'east'  : 'Garden',
                  'item'  : 'monster'
                },
                
            'Dining Room' : {
                  'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'shield'
            },
            
            'Garden'  : {
                   'north'    : 'Dining Room',
                   'west'     : 'Kitchen'
            }

         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
 # player loses if they if they enter a room with a monster
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
   print ('A monster has got you... GAME OVER!')
   break
 
 #player wins if they get to the garden with a key and a shield
  if currentRoom == 'Garden' and 'key' in inventory and 'shield' in inventory:
    print('''
    ╓ww   ,ww                       ╓w,   ╓ww    ww                     ║║║
    ╙░▒║ ╓▒▒▒    ,,     ,    ,      ▒▒░  ]░░░W  ║▒▒░   ,,,     ,  ,,    ╢▒▒
     ░▒▒▒▒▒▒░ ╓╢░░░║╢W ║▒▒  ]▒▒w    ]▒▒[ ╢▒▒▒▒ ,▒▒▒ ,║░░░░╢N  ▒▒╢░░║╢w  ▒▒▒
      ░▒▒▒▒░ ]▒▒▒░╙▒▒▒w╢▒▒  ]▒▒      ▒▒▒]▒▒▒▒▒▒╢▒▒░ ▒▒▒░`░▒▒@,▒▒▒░░▒▒▒  ╢▒▒
       ╢▒░░  ╙▒▒║ ,║▒▒░╢▒▒W,║▒▒      ╙▒░▒░▒░╢░░▒░░  ▒▒░, ╓░▒Ñ░▒▒▒  ▒▒▒  ║Ñ░
       ╢░▒    ░░░░░░░░ '░░░░║▒▒░      ╢░░▒░  ▒░░▒   ░░░░░░░Ñ` ▒░░  ▒░▒  ╢░▒
        ``      `╙╙`     `╙````        ```    ``      ``╙``   '`   '`    ``
                            You Won!
    ''')
    print('''
           ,,    ,,   ,,        ,µ╖ ╓µ╓     ,,,,                             ╓╓
      ]▒ ▒  ▒ ]W ║Ñ╢`       ╠H╢ ▒ ▒    ▒ ╓▒▒░╙N                         ║▌][
       ▒L╢w╟M@ ▒ ▒ ▒ ╓M▒▒▒╢y╠H╢ ▒ ▒    ▒ ▒ `▒▒ N╓Ñ░▒▒╙╫ ▒░▒▒╓`║ ,Ñ░▒▒╙W ]▒]h
       ╙▒ ▒▒║▒▒]▒▒╢ ]▒]▒▒▒,▒╠k╢ ▒░▒    ▒ ▒  ]▒,▒▒ ▒ ░▒ ▒▒H▒`]▒]M▒ ▒▒▒▒▒ ]▒⌠h
        ▒▒░░▒ ▒░▒░▒ ]▒░▒▒▒▒╖╠░▒ ▒░▒    ▒░▒╖0▒░▒░▒░▒╖@░║`▒░▒ ]▒░░▒W▒▒▒▒▒ )▒▒µ
         ▒▒▒` ╙▒▒Ñ   ╙▒▒Ñ▒Ñ ░▒Ñ ▒▒╜    ▒▒▒▒Ñ╜`  `M▒Ñ▒Ñ` ░▒Ñ ╙▒▒ `M▒ÑÑ▒╙ ╙▒▒

                            Well Done!
    ''')
    print('Thanks for playing!')
    print('Tweet me if there are any issues')
    print('@ThisIsNoahEvans')
    print('Feel free to remix any projects!')
    print('And don\'t forget to share with your friends!')
    break

  elif currentRoom == 'Garden':
   print('Well done, you made it to the garden. But you need both a key and a shield. Type \'go north\' to exit the garden.')

#Will be focusing on scopes and how to utilize them


enemies = 1

def increase_enemies():
    enemies = 2
    print(f'Enemies inside function: {enemies}')

#Prints enemies as 2 because we are still in function
increase_enemies()
#Outside the function though the enemies is still 1
print(f'Enemies outside function: {enemies}!')


#Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

#This will throw an error because the variable potion_strength is declared in that function and only exist in that function
#print(potion_strength)

#Global Scope
#This variable is declared and anything written after this can access this variable now
player_health = 10

def help_health():
    potion_strength = 2
    print(player_health)

help_health()
print(player_health)


#Thees is no block scope in python

if 3 > 2:
    a_variable = 10

game_level = 3
enemies = ['skeletons', 'zombies', 'alien']
def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]
    print(f'new enemy is :{new_enemy}')

#This will not work because it is outside the block it is created in
#print(new_enemy)


#Modifying global scopw

enemies = 'skeleton'

def increase_enemies():
    #With this keyword we can modify variables outside the scope
    #It cna be confusing and lead to bugs
    # global enemies
    # enemies += 1

    #To avoid using the above you can use the return statement
    #return enemies += 1
    
    enemies = 'zombies'
    
    print(enemies)

increase_enemies()
print(enemies)


#Global Constants
#To name a constant you use all caps and separate with underscores
PI = 3.14159


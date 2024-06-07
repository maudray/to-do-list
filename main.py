import program
print("To-do list")
# get the user choice 

     

while True:
   program.display_menu()
   user_option = int(input ("select an option to proceed\n"))
   if user_option == 1:
       program.add_task()
   elif user_option == 2:
       program.view_task()
   elif user_option == 3:
      pass
   elif user_option == 4:
      pass
   elif user_option == 5:
         exit()
   else:
      print("invaild number enter a number between 1 - 5")

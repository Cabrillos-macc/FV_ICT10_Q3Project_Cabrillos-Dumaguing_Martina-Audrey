from pyscript import document
from js import eval as js_eval

#This is a list that functions to store created accounts to avoid repeation of the same information.
accounts = []

def validate_account(username, password):
 #This checks that the username must at least be 7 characters long.
 #len checks the lenght of number of elements.
 if len(username) < 7:
     missing = 7 - len(username) #If the user name is less than 7, it will calculate how many characters are missing.
     return f"Username needs {missing} more character(s)." #If the statement is right, it will return this message.


 #This checks if the password is less than 10 characters.
 if len(password) < 10:
     missing = 10 - len(password) #If the password is less than 10, it will calculate how many characters are missing.
     return f"Password needs {missing} more character(s)." #If the statement is right, it will return this message.


 #This now checks if the password contains a letter (a-z).
 letter = any(char.isalpha() for char in password) #This basically collects the values needed to check.
 if not letter: #If ever no letter is found, this if statement will be executed by python.
     return "Password must contain at least one letter." #It will return this message if the if statement is executed.


 #This checks if there are numerical values found in the password.
 number = any(char.isdigit() for char in password) #This identifies the password and checks if there are numerical values.
 if not number: #If no numerical values are found, this if statement will activate.
     return "Password must contain at least one number." #It will also return this message if the statement is executed.


 return "Valid" #If everything complies with the rules and doesn't satisfy the if statements, this will return.

#This is the py-click or button. When clicked, this block of code will function and be read.
def information(event):
 #My code keeps refreshing when it executes so this helps it prevent it.
 #I am unsure if the refreshing was wifi or my device but this solved it.
 #It helps prevent my website from going back to its default or refreshing.
 #This is also helps as memory for my website to remember the previous information inputed.
 event.preventDefault()
 email_input = document.getElementById("account") #These are variables that collects data from my HTML ids.
 password_input = document.getElementById("pass") #These are variables that collects data from my HTML ids.
 result_list = document.getElementById("account-creation") #These are variables that collects data from my HTML ids.
 email = email_input.value.strip() #This gets the information inputed by the user as well as removes the extra spaces found before and after it.
 password = password_input.value.strip() #This gets the information inputed by the user as well as removes the extra spaces found before and after it.
 result_list.innerHTML = "" #This avoids multiple messages to be stacked up if user tries using the form more than one time.

 if email == "" or password == "": #This condition only takes place if the input fields are left empty.
     result_list.innerHTML = "<li style='color:#5e0704;'>All fields are required.</li>"


 elif "@" not in email or "." not in email: #This condition only takes place if @ or . is not read in the email field.
     result_list.innerHTML = "<li style='color:#5e0704;'>Invalid email format.</li>"


 else: #This checks if everything is valid and is okay with all conditions.
     validation_result = validate_account(email, password)


     if validation_result != "Valid": #if the validation_result does not come back as valid, this code will be executed.
         result_list.innerHTML = f"<li style='color:#5e0704;'>{validation_result}</li>" #Basically calls for the validation_result variable which holds the data needed.
         return


     account_exists = False #This assumes that the account does not exist for now. It serves as a blank slate for my data.
     for acc in accounts: #This goes back to the accounts variable at the very start of my code.
         if acc["email"] == email:
             account_exists = True


     if account_exists: #If the system reads the account to have been added to the system, it executes this.
         result_list.innerHTML = "<li style='color:#5e0704;'>Account already exists.</li>"
     else: #This checks the data from input fields and if valid, it adds the account to the accounts variable in the very start of my code.
         accounts.append({
             "email": email,
             "password": password
         })


         result_list.innerHTML = "<li style='color:green;'>Account created successfully! You may now log in.</li>"


         #this triggers the confetti effect when the account is successfully created
         js_eval("""
         confetti({
             particleCount: 180,
             spread: 100,
             origin: { y: 0.6 },
             colors: ["#5e0704", "#a64451", "#f0e9d5"]
         });
         """)


         #Once the account has been made, this will be excuted to make the input fields empty once again.
         email_input.value = ""
         password_input.value = ""

#This is a code that activates once the button named "team_info" has been clicked by the user.
def team_info(e):
 regone = document.getElementById("reg_one").checked #The data for this variable comes from the registration of YES in my HTML.
 regtwo = document.getElementById("reg_two").checked #The data for this variable comes from the registration of NO in my HTML.
 medone = document.getElementById("med_one").checked #The data for this variable comes from the medical of YES in my HTML.
 medtwo = document.getElementById("med_two").checked #The data for this variable comes from the medical of NO in my HTML.
 grade = document.getElementById("grade").value #The data used for this variable is taken from the grade dropdown located in my HTML structure.
 section = document.getElementById("section").value #The data used for this variable is taken from the section dropdown located in my HTML structure.
 result = document.getElementById("result") #Data found here is in the div function with the id "result" found in my HTML structure.
 #this allows pyscript to organize a specific grade and section to a specific intrams team.
 team_mapping = {
     #Grade 7
     ("seven", "emerald"): "Red Bulldogs",
     ("seven", "ruby"): "Yellow Tigers",
     ("seven", "sapphire"): "Blue Bears",
     ("seven", "topaz"): "Green Hornets",
     #Grade 8
     ("eight", "emerald"): "Green Hornets",
     ("eight", "ruby"): "Blue Bears",
     ("eight", "sapphire"): "Red Bulldogs",
     ("eight", "topaz"): "Yellow Tigers",
     ("eight", "jade"): "Red Bulldogs",
     #Grade 9
     ("nine", "emerald"): "Red Bulldogs",
     ("nine", "ruby"): "Blue Bears",
     ("nine", "sapphire"): "Green Hornets",
     ("nine", "topaz"): "Yellow Tigers",
     ("nine", "jade"): "Red Bulldogs",
     #Grade 10
     ("ten", "emerald"): "Red Bulldogs",
     ("ten", "ruby"): "Green Hornets",
     ("ten", "sapphire"): "Yellow Tigers",
     ("ten", "topaz"): "Blue Bears",
 }
 #this connects the team name to the assigned/paired photo.
 team_images = {
     "Yellow Tigers": "tiger.png",
     "Red Bulldogs": "bulldog.png",
     "Blue Bears": "bears.png",
     "Green Hornets": "hornet.png" }
 #this connects each team to a set of confetti colors so the confetti matches the team
 #Each team has 3 shades of their color for a nicer visual effect.
 team_colors = {
     "Yellow Tigers": ["#eab308", "#fde047", "#facc15"],
     "Red Bulldogs": ["#dc2626", "#ef4444", "#f87171"],
     "Blue Bears": ["#2563eb", "#3b82f6", "#60a5fa"],
     "Green Hornets": ["#16a34a", "#22c55e", "#4ade80"]
 }
  #This sets up the code to your assigned team and information based on your selection and data input on the form.
 team = team_mapping.get((grade, section))
 #This finds for the grade id and section id which holds the values needed to perform the code.
 img_src = team_images.get(team, "schoollogo copy.png")
 #This ensures that the assigned images to the teams will be done.
 #Note: the "schoollogo copy.png" is for when the action "none" or when one area is not filled up by the user. This allows us to see the OBMC logo instead.
 team_image_html = f"<br><img src='{img_src}' style='width:300px; margin-top:10px;'>"
 #if-elif-else
 #The conditions done by this code depends on the registration, medical, grade, and section.
 #If ever user leaves all areas of the form as blank, this will proceed to the second elif condition.
 #Once they have decided to fullfill what the second elif condition has given, this will still not give them their team as it will proceed to else condition IF first elif is not satisfied.
 if regone and medone:
     result.innerHTML = f"You are part of <b>{team}</b>!!!!!! {team_image_html}" #This takes place when they have complied with all areas of the form.
     #this triggers the confetti effect when the user successfully sees their team
     #canvas-confetti is a javascript library that creates the confetti animation on screen.
     colors = team_colors.get(team, ["#5e0704", "#f0e9d5"]) #gets the team's colors, or defaults to OBMC colors if team is not found.
     colors_js = str(colors) #this converts the Python list into a string so JavaScript can read it.
     js_eval(f"""
     confetti({{
         particleCount: 150,
         spread: 80,
         origin: {{ y: 0.6 }},
         colors: {colors_js}
     }});
     """)
     #particlecount controls how many confetti pieces appear
     #spread controls how wide the confetti spreads out
     #origin sets where the confetti comes from
     #colors makes the confetti match the team's colors!

 elif regtwo or medtwo:
     result.innerHTML = f""" ⚠️You are part of <b>{team}</b>. Sadly, you will not be permitted to join
     the team fully until you comply with all requirements. Kindly double check what requirement/s you
     lack and make the necessary appoitments to fullfill this. {team_image_html}""" #This takes place when they have placed "NO..." in one or both of the checkboxes.
 elif grade == "none" or section == "none":
     result.innerHTML = "🚨 Please select both grade and section. 🚨" #This takes place when they did not input the grade & section or if they left everything blank.
     return
 else:
     result.innerHTML = "Please answer all the requirements." #This takes place when they only answered grade & section and left the registration and medical as blank.

#N-O-T-E:⬇︎
#If user fails to input the grade and sction BUT inputs in the registration and medical,
#it would say "You are part of NONE" because this is meant to show you that you may have the requirements
#but not having a class (grade & section) means you may not be part of OBMC (as an assumption).

players = [
 "Andes : 10 Topaz | Male | Volleyball",
 "Ayala : 10 Topaz | Male | Basketball",
 "Cabrillos : 10 Topaz | Female | Badminton",
 "Daed : 10 Topaz | Female | Volleyball",
 "Damondamon : 10 Topaz | Female | Dodgeball",
 "De Jesus : 10 Topaz | Male | Basketball",
 "Deray : 10 Topaz | Male | Badminton",
 "Dumaguing : 10 Topaz | Female | Volleyball",
 "Ecraela : 10 Topaz | Female | Hula Hoop Relay",
 "Escarda : 10 Topaz | Male | Basketball",
 "Fabul : 10 Topaz | Female | Kadang-Kadang",
 "Ferrer : 10 Topaz | Female | Volleyball",
 "Gorom : 10 Topaz | Male | Badminton",
 "Grande : 10 Topaz | Male | Badminton",
 "Ligas : 10 Topaz | Male | Volleyball",
 "Manese : 10 Topaz | Female | Hula Hoop Relay",
 "Mendez : 10 Topaz | Female | Volleyball",
 "Noble : 10 Topaz | Female | Tug of War",
 "Salapunen : 10 Topaz | Male | Volleyball",
 "Santos : 10 Topaz | Female | Volleyball",
 "Tacan : 10 Topaz | Male | Volleyball",
 "Taruc : 10 Topaz | Male | Basketball",
 "Tenorio : 10 Topaz | Male | Volleyball",
 "Tiongson : 10 Topaz | Male | Kadang-Kadang",
 "Ubana : 10 Topaz | Female | Volleyball",
 "Villanueva : 10 Topaz | Female | Badminton",
 "Zales : 10 Topaz | Male | Volleyball"
]

def show_players(event=None):
 player_list = document.querySelector("#players-list")
 player_list.innerHTML = ""

 for name in players:
     li = document.createElement("li")
     li.innerText = name
     player_list.appendChild(li)

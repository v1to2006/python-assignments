target_user_name = "Trump"
target_password = "Skibidi67"
retries_count = 5
valid_credentials = False

while retries_count > 0:
	input_user_name = input("Enter username: ")
	input_password = input("Enter password: ")

	if input_user_name == target_user_name and input_password == target_password:
		valid_credentials = True
		break
	
	retries_count -= 1
	print(f"Wrong username or password. Attempts left: {retries_count}")

if (valid_credentials):
	print("Welcome!")
else:
	print("Access Denied")

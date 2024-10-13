from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# YOUR CODE BELOW

password_found = False # flag to indicate if the correct password was found
k = 0 # instantiate counter

for i in range(97, 123):
    for j in range(97, 123):
        
        find_me = chr(i) + chr(j)
        secret_password = find_me + 'bcmpda'
        k +=1
        if unzip_with_7z(zip_file_path, dest_path, secret_password) == True:
            print(f"number of tries is {k}")
            password_found = True
            break # exit the loop if the password is correct
            
    if password_found:
        break # exit the loop completelly
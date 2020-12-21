##imports
import os
import datetime
from datetime import *
import shutil 

##params
dir1 = r'C:\Users\Chris\scripts\github\if_exists_move\directory1' ##Directory containing file to move
dir2 = r'C:\Users\Chris\scripts\github\if_exists_move\directory2' ##Destination directory
file_to_check = r'C:/Users/Chris/scripts/github/if_exists_move/directory2/file_to_replace.txt' ##File to check if exists
file_to_move = r'C:/Users/Chris/scripts/github/if_exists_move/directory1/file_to_move.txt' ##File to move

##logic
if os.path.exists(file_to_check): ##check if the file exists
    os.remove(file_to_check) ##remove file being replaced
    shutil.move(file_to_move,dir2) ##move the file to new location
    print(f"{datetime.now()} {file_to_move} has been moved from {dir1} to {dir2} and replaced {file_to_check}") ##output file has been moved
else:
    print(f"{file_to_check} does not exist") ##Enter else if file does not exist
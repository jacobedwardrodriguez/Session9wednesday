# reading files
fp = open("text.txt", "r") # r is by default, not really needed (r=reading)
print(fp.read()) # prints the entire content of the file
fp.close() # good practice to close the file

# same exact with context manager
with open("text.txt", "r") as fp: #fp = file pointer
    print(fp.read())

# ^ basically just saves you the requirement to use 'close'

# let's read from the same file, line by line

print("Read the file line by line")
line_number = 1
with open ("text.txt", "r") as fp:
   for line in fp: # we iterate over the file, line by line
        print(f"{line_number}: {line}", end="") # ask print to add new line
        # print(line.rstrin())
        line_number += 1
       # print(line) # ', end=""' asks print not to add a new line

print("done printing")

# now we have numbered the lines of text
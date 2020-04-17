# smartsnek
Python CLI tool for looking up word definitions

# Setting up

1. On linux machine, clone the repo with command `git clone https://github.com/gigamarr/smartsnek`
2. Create symlink for `__main__.py` and place it on the system path, for exampe `ln -s /home/user/smartsnek/__main__.py /usr/bin/snek`

### Usage
- You can call the command with `snek <word>`
- Some words output hundreds of definitions, if you want to output only the first N number of definitions you can do it with `-c` argument, for example `snek <word> -c 5`
### Writing to a file
- Suppose you want to write 4th definition of the word levity to a file silently, you would be able to do it the following way:
`snek levity --write --index 4 -s` which would result in a new file called `output` to be created wherever your smartsnek lives.

# smartsnek
Python CLI tool for looking up word definitions

# Setting up

1. On linux machine, clone the repo with command `git clone https://github.com/gigamarr/smartsnek`
2. Create symlink and place it on the system path, for exampe `ln -s /home/user/smartsnek/__main__.py /usr/bin/snek`
3. Call it with command `snek <word>`

# Usage

Some words output hundreds of definitions, if you want to output only the first N number of definitions you can do it with `-c` argument, for example `snek <word> -c 5`

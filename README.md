### This is a simple python script to 'automate' a few git utils

This was created mainly for educational purpouses and to be used alongside with
bash aliases on the a-shell iOS app

## Instalation

If you want to use this, simply add the script to ~/Documents/bin on your
iOS devide (addapt to use it anywhere else). Then add the following to your
`.bashrc` file: 
```ruby
alias add="python3 ~/Documents/bin/gutils-main.py add"
alias add="python3 ~/Documents/bin/gutils-main.py add"
alias commit="python3 ~/Documents/bin/gutils-main.py commit"
alias push="python3 ~/Documents/bin/gutils-main.py push"
alias pull="python3 ~/Documents/bin/gutils-main.py pull"
alias branches="python3 ~/Documents/bin/gutils-main.py branches"
alias status="python3 ~/Documents/bin/gutils-main.py status"
alias st="python3 ~/Documents/bin/gutils-main.py status"
alias gitutils="python3 ~/Documents/bin/gutils-main.py gitutils"
alias gutils="python3 ~/Documents/bin/gutils-main.py gitutils"
``` 

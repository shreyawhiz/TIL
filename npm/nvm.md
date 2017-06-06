## In Mac

````javascript
brew install nvm
mkdir ~/.nvm
nano ~/.bash_profile
````

In your .bash_profile file (you may be using an other file, according to your shell), add the following :

````javascript
export NVM_DIR=~/.nvm
source $(brew --prefix nvm)/nvm.sh
````

Back to your shell, activate nvm and check it (if you have other shells opened and you want to keep them, do the same) :

````javascript
source ~/.bash_profile
echo $NVM_DIR
````

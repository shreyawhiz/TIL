## To configure subl command (open Sublime Text from cli itself

### Either create a linker file

````javascript
ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl
````


OR


### create an alias in the bash/zsh profile file
````javascript
alias subl="/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl"
````


But when using some external library, let say for example pet command, profile files are not loaded in the environment, and hence subl command won't work of an alias has been created.

However, linker file would load perfectly fine.

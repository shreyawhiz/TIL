To find What Shell Is Being Used in Mac OS X, Unix, Linux
```javascript
echo $SHELL
```


Setting up MAMP-PRO

While starting it was giving error that apache could not be started and there was nothing in the apache-server logs as well.
Upon searching, found the following solution thta fixed it

```javascript
mv /Applications/MAMP/Library/bin/envvars  /Applications/MAMP/Library/bin/_envvars
```




## pet command module

````javascript
pet help

Usage:
  pet [command]

Available Commands:
  configure   Edit config file
  edit        Edit snippet file
  exec        Run the selected commands
  help        Help about any command
  list        Show all snippets
  new         Create a new snippet
  search      Search snippets
  sync        Sync snippets
  version     Print the version number
  
Flags:
      --config string   config file (default is $HOME/.config/pet/config.toml)
      --debug           debug mode
      


## To edit pet snippets in Sublime Text

cat $HOME/.config/pet/config.toml

[General]
  snippetfile = "/Users/shreyabatra/.config/pet/snippet.toml"
  editor = "vim"
  column = 40
  selectcmd = "peco"

[Gist]
  file_name = "pet-snippet.toml"
  access_token = ""
  gist_id = ""
  public = false
  
  
  
  
  subl /Users/shreyabatra/.config/pet/snippet.toml
  
 

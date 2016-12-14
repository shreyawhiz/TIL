## Life Saving Commands if you by mistake git stash twice ##

`1. git stash list`

		Lists all the git stashes you have stored
		For instance,
			$ git stash list
			stash@{0}: WIP on master: 049d078 added the index file
			stash@{1}: WIP on master: c264051 Revert "added file_size"
			stash@{2}: WIP on master: 21d80a5 added number to log
		
		
`2. git stash show`
		To show the content of a stash
		
`3. git stash save "example stash name"`
		To give a name to your stash
		
`4. git stash apply`
		To get the changes from the last stash.
		
`5. git stash apply stash@{1}`
		To get the changes from a random stash.

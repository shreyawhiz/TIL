`$ git push origin --delete <branch_name>`

`$ git branch -d <branch_name>`

The -d option is an alias for --delete, which only deletes the branch if it has already been fully merged in its upstream branch.
You could also use -D, which is an alias for --delete --force, which deletes the branch "irrespective of its merged status." [Source: man git-branch]

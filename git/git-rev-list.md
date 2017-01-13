`git-rev-list` 

  Lists commit objects in reverse chronological order.
  
 In case you want to see the first commit on a project, do this :
 
 `git rev-list --max-parents=0 HEAD`
 
 *Show me the commits that led to* `HEAD` *in reverse chronological order; then limit that list to the commits with no parent.*

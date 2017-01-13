# Undo a Git Mistake

`git reflog` is a record of your actions in Git. With this command, you can undo almost any Git mistake.

```
$ git reflog

670e9f0 HEAD@{0}: <bad place>
6c00ce4 HEAD@{1}: <bad place>
4df81db HEAD@{2}: <last good place>
3c1f4c4 HEAD@{3}: <good place>
6f87d14 HEAD@{4}: <good place>

$ git reset --hard HEAD@{2}
```

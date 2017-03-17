The answer to this is `git reflog`
(https://git-scm.com/docs/git-reflog)

Use the `reflog` for the branch

For instance if I had just rebased mybranch, I would see:

$ git reflog mybranch
nnnnnnn mybranch@{0}: rebase finished: refs/heads/mybranch onto biguglysha1
ooooooo mybranch@{1}: commit: some sort of commit message

If you then:

$ git checkout mybranch # if needed

and:

$ git reset --hard ooooooo  # or mybranch@{1}

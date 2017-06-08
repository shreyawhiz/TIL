The rules in your **.gitignore** file only apply to untracked files. Since the files under that directory were already committed in your repository, you have to unstage them, create a commit, and push that to GitHub:

````javascript
git rm -r --cached some-directory
git commit -m 'Remove the now ignored directory "some-directory"'
git push origin master

````
You can't delete the file from your history without rewriting the history of your repository - you shouldn't do this if anyone else is working with your repository, or you're using it from multiple computers. If you still want to do that, you can use git filter-branch to rewrite the history - there is a helpful guide to that here.

Additionally, note the output from git rm -r --cached some-directory will be something like:

````javascript
rm 'some-directory/product/cache/1/small_image/130x130/small_image.jpg'
rm 'some-directory/product/cache/1/small_image/135x/small_image.jpg'
rm 'some-directory/.htaccess'
rm 'some-directory/logo.jpg'

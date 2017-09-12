```javascript
mongoexport -d test -c articles --type=csv --fields _id,title,slug,wpId,Tags,Categories,provider -q '{Tags:{$size:0}}' --out articlesWithoutTags.csv


mongoexport -d test -c articles --type=csv --fields _id,title,slug,wpId,Tags,Categories,provider -q '{Categories:{$size:0}}' --out articlesWithoutCategories.csv


mongoexport -d test -c posts --type=csv --fields _id,title,slug,wpId,Tags,Categories,provider -q '{Tags:{$size:0}}' --out postsWithoutTags.csv



mongoexport -d test -c articles --type=csv --fields _id,title,slug,wpId,Tags,Categories,provider -q '{Tags:{$size:0}, Categories:{$ne:ObjectId("55e9303c98512d22hrhfnb8j")}}' --out articlesWithoutTags.csv


mongoexport -d test -c posts --type=csv --fields _id,title,slug,wpId,Tags,Categories,provider -q '{curated:true,Tags:{$size:0}}' --out postsWithoutTags.csv


-d database name
-c collection name
--fields fields to export
-q filter collection by query
--out export to the file

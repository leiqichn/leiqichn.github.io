git add .
git commit -m "update"
git push origin master
git push github master

sleep 60
git checkout gh-pages
git add . 

git commit -m "update"
git push origin master

git checkout master

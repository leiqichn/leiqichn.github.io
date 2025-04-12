
git add . 
git commit -m "gitee update master"
echo "###push gitee master###"
git push gitee master
git checkout gh-pages
echo "###pull gitee gh-pages###"
git pull origin gh-pages
git add . 
git commit -m "gitee update gh-pages"
echo "###push gitee gh-pages###"
git push gitee gh-pages

git checkout master

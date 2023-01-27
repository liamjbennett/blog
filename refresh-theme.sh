if [ -d "themes/hugo-PaperMod" ]
then
    git submodule deinit -f themes/hugo-PaperMod
    cd themes
    git rm hugo-PaperMod
    rm -rf hugo-PaperMod
    rm -rf .git/modules/themes/hugo-PaperMod
else
    git submodule add https://github.com/adityatelange/hugo-PaperMod
fi
if [ -d "themes/hugo-PaperMod" ]
then
    git submodule deinit -f themes/hugo-PaperMod
    cd themes
    git rm -f hugo-PaperMod
    rm -rf hugo-PaperMod
    rm -rf .git/modules/themes/hugo-PaperMod
else
    cd themes
    git submodule add --force https://github.com/adityatelange/hugo-PaperMod
fi
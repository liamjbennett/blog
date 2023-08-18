#
# brew install asciidoctor
# brew install pandoc
# gem install asciidoctor-pdf

cat > ./header.md <<- EOM
---
ShowShareButtons: false
ShowReadingTime: false
ShowPostNavLinks: false
ShowBreadCrumbs: false
ShowCodeCopyButtons: false
ShowToc: true
author: "."
---

EOM

for TYPE in long short; do
  asciidoctor --backend docbook -a $TYPE --out-file docbook.xml cv.adoc
   sed -i '' '/<date>/d' ./docbook.xml
  pandoc --from docbook --to docx --reference-doc=reference.docx  --output liamjbennett-cv-$TYPE.docx docbook.xml
  asciidoctor-pdf --theme ./asciidoctor-theme.yml -a $TYPE -o liamjbennett-cv-$TYPE.pdf cv.adoc
  asciidoctor -b docbook cv.adoc -a $TYPE -o cv-$TYPE.xml
  pandoc -f docbook -t markdown_strict cv-$TYPE.xml -o cv-tmp.md
  
  echo "{{< cv_page word_file=\"/cv/liamjbennett-cv-$TYPE.docx\" pdf_file=\"/cv/liamjbennett-cv-$TYPE.pdf\" >}}\n" >> ./$TYPE-prefix.md

  cat header.md $TYPE-prefix.md cv-tmp.md >> $TYPE.md
  rm cv-$TYPE.xml $TYPE-prefix.md cv-tmp.md
  
  mv $TYPE.md ../content/cv/$TYPE.md
  mv liamjbennett-cv-$TYPE.docx ../static/cv/liamjbennett-cv-$TYPE.docx
  mv liamjbennett-cv-$TYPE.pdf ../static/cv/liamjbennett-cv-$TYPE.pdf
done

rm ./header.md
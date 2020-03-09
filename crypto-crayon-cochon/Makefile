all:
	xelatex chall.tex
	pdftoppm chall.pdf chall -png
	mv chall-1.png chall.png

clean:
	rm *.aux *.log chall.pdf *~

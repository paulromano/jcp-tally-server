# Name of manuscript
manuscript = jcp-tally-server

# List of images to be included
images = model_intrepid.pdf model_titan.pdf results_titan_r1.pdf \
   results_titan_r3.pdf results_titan_r7.pdf results_titan_r15.pdf \
   results_titan_cs.pdf results_intrepid_r1.pdf results_intrepid_r3.pdf \
   results_intrepid_r7.pdf results_intrepid_r15.pdf results_intrepid_cs.pdf \
   results_baseline.pdf

# PdfLaTeX compilation options
latexopt = -halt-on-error -file-line-error

#=================================================================
# Generate PDF of manuscript using PdfLaTeX
#=================================================================

all: $(manuscript).pdf

$(manuscript).pdf: $(manuscript).tex $(images) references.bib
	pdflatex $(latexopt) $(manuscript)
	bibtex -terse $(manuscript)
	pdflatex $(latexopt) $(manuscript)
	pdflatex $(latexopt) $(manuscript)

#=================================================================
# Generate Images
#=================================================================

model_%.pdf: model_%.py
	python $<

results_titan_%.pdf: results_titan.py
	python $<

results_intrepid_%.pdf: results_intrepid.py
	python $<

results_baseline.pdf: results_baseline.py
	python $<

#=================================================================
# Other
#=================================================================

clean:
	@rm -f *.aux *.bbl *.blg *.log *.out *.spl \
    $(manuscript).pdf results_*.pdf model_*.pdf

.PHONY: all clean

clean:
	@rm *.html
	@echo "Cleaned old files."
	
all: clean
	@cd content-generator/src; python main.py
	@echo "New files were created."
	
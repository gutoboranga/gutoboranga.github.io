all:
	@cd content-generator/src; python main.py
	@echo "New files were created."
	
clean:
	@rm *.html
	@echo "Cleaned old files."

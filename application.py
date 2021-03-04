from src import create_app as application
	
if __name__ == '__main__':
	application=create_app()
	application.debug=True
	application.run()
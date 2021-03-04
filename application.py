from src import create_app as application
	
if __name__ == '__main__':
	application=application()
	application.debug=True
	application.run()
# Entry point to set up and run the Flask application

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

Country REST API

A Python project integrated with the CountryLayer API to retrieve information about countries based on user input. The retrieved data is displayed directly in the console.

Features

Search for country information using user input

Integration with the CountryLayer API

Display retrieved information in the console

Secure API key management using python-dotenv

Technologies Used

Python

CountryLayer API

Requests

python-dotenv

Configuration

Clone the repository.

Create and activate a virtual environment.

Install the required dependencies:

pip install -r requirements.txt

Create a .env file in the project root and add your CountryLayer API key:

COUNTRYLAYER_API_KEY=your_api_key_here

Ensure the application loads environment variables using python-dotenv.

Run the Python script and enter a country name when prompted.

Environment Variables

The API key is stored in .env rather than being hardcoded into the source code.

API Availability Notice

This project uses the CountryLayer API to retrieve country information. The API may return errors if the access key is invalid, expired, or requires an active subscription.

If the API no longer works because of changes to the service, access restrictions, or an outdated API key, this does not necessarily indicate a bug in the project's code. Please check your API key and the current CountryLayer service requirements.
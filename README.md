# Stock Notifier

This project fetches the latest stock price for a specified company and sends an SMS alert via Twilio if there is a significant change (currently any change, as the condition is hard-coded to `True`). The SMS contains a brief on the latest news related to the company.

## Features

- Fetch stock prices using the Alpha Vantage API.
- Fetch the latest news using the News API.
- Send SMS alerts via Twilio when there is a significant stock price change.
- All sensitive information (like API keys) are stored in environment variables for security.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/GerardoBZentenoM/Stock-Trading-News-Alert.git
    ```
2. Change the working directory to the project's root directory:
    ```
    cd Stock-Trading-News-Alert
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Create a `.env` file and add the required environment variables:
    ```
    ALPHA_VANTAGE_API_KEY = "your_alpha_vantage_api_key"
    NEWS_API_KEY = "your_news_api_key"
    TWILIO_SID = "your_twilio_sid"
    TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
    TWILIO_PHONE_NUMBER = "your_twilio_phone_number"
    RECIPIENT_PHONE_NUMBER = "recipient_phone_number"
    ```

## Usage

Run the main script:
```
python main.py
```

## Environment Variables

- `ALPHA_VANTAGE_API_KEY`: Your Alpha Vantage API key.
- `NEWS_API_KEY`: Your News API key.
- `TWILIO_SID`: Your Twilio SID.
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token.
- `TWILIO_PHONE_NUMBER`: Your Twilio phone number, from which the SMS alert will be sent.
- `RECIPIENT_PHONE_NUMBER`: The recipient's phone number, to which the SMS alert will be sent.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT

## Contact

Please feel free to contact the maintainer of this project for any kind of inquiries or support.

## Note

This is a basic version of the project, there are several improvements that can be made, such as:

- Use the `schedule` library to run the script at a particular time every day.
- Create a GUI or web interface to display the data instead of printing it in the console.
- Use a database to store the stock prices for further analysis in the future.
- Add exception handling to manage potential errors better.
- Implement unit tests to ensure everything is working as expected.
- Implement logging to keep track of when and why certain actions/decisions were taken.

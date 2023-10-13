import os
import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Retrieve your CoinMarketCap API key from environment variables
    api_key = os.environ.get("cmcapikey")
    
    # Check if the API key is set
    if api_key is None:
        return func.HttpResponse("CoinMarketCap API key not found.", status_code=500)
    
    # Set the API endpoint URL
    api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    
    # Set the request headers with the API key
    headers = {
        'X-CMC_PRO_API_KEY': api_key
    }
    
    try:
        # Make the API request
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        
        # Return the response as JSON
        return func.HttpResponse(response.text, mimetype="application/json", status_code=200)
    
    except requests.exceptions.RequestException as e:
        return func.HttpResponse(f"Error making the API request: {str(e)}", status_code=500)

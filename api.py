{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f4cb2b2b",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'azure'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mos\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mrequests\u001b[39;00m\n\u001b[1;32m----> 3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mazure\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mfunctions\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mfunc\u001b[39;00m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mmain\u001b[39m(req: func\u001b[38;5;241m.\u001b[39mHttpRequest) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m func\u001b[38;5;241m.\u001b[39mHttpResponse:\n\u001b[0;32m      6\u001b[0m     \u001b[38;5;66;03m# Retrieve your CoinMarketCap API key from environment variables\u001b[39;00m\n\u001b[0;32m      7\u001b[0m     api_key \u001b[38;5;241m=\u001b[39m os\u001b[38;5;241m.\u001b[39menviron\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcmcapikey\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'azure'"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import requests\n",
    "import azure.functions as func\n",
    "\n",
    "def main(req: func.HttpRequest) -> func.HttpResponse:\n",
    "    # Retrieve your CoinMarketCap API key from environment variables\n",
    "    api_key = os.environ.get(\"cmcapikey\")\n",
    "    \n",
    "    # Check if the API key is set\n",
    "    if api_key is None:\n",
    "        return func.HttpResponse(\"CoinMarketCap API key not found.\", status_code=500)\n",
    "    \n",
    "    # Set the API endpoint URL\n",
    "    api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'\n",
    "    \n",
    "    # Set the request headers with the API key\n",
    "    headers = {\n",
    "        'X-CMC_PRO_API_KEY': api_key\n",
    "    }\n",
    "    \n",
    "    try:\n",
    "        # Make the API request\n",
    "        response = requests.get(api_url, headers=headers)\n",
    "        response.raise_for_status()\n",
    "        \n",
    "        # Return the response as JSON\n",
    "        return func.HttpResponse(response.text, mimetype=\"application/json\", status_code=200)\n",
    "    \n",
    "    except requests.exceptions.RequestException as e:\n",
    "        return func.HttpResponse(f\"Error making the API request: {str(e)}\", status_code=500)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7bf6890f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

from django.core.management.base import BaseCommand, CommandError
import json
import os
from show_financial_models.models import EODData  # Assuming the model is in this location

class Command(BaseCommand):
    help = 'Loads EOD stock data from JSON files into the database'

    def handle(self, *args, **options):
        # Base path to the 'sample-data' directory (You'll need to specify this)
        sample_data_path = '../sample-data'

        # Get the list of all tickers (subdirectories) in 'sample-data'
        tickers = [d for d in os.listdir(sample_data_path) if os.path.isdir(os.path.join(sample_data_path, d))]

        for ticker in tickers:
            json_file = os.path.join(sample_data_path, ticker, 'eod.json')

            # Load JSON data from file
            with open(json_file, 'r') as f:
                eod_data = json.load(f)

            # Insert data into the database
            for record in eod_data:
                EODData.objects.create(
                    symbol=ticker.upper(),
                    date=record['date'],
                    open=record['open'],
                    high=record['high'],
                    low=record['low'],
                    close=record['close'],
                    adjusted_close=record['adjusted_close'],
                    volume=record['volume']
                )

            self.stdout.write(self.style.SUCCESS(f'Successfully imported EOD data for {ticker.upper()}'))


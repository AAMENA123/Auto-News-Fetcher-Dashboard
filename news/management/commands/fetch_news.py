from django.core.management.base import BaseCommand
from news.views import NewsFetcher

class Command(BaseCommand):
    help = 'Fetches latest news from NewsAPI'
    
    def handle(self, *args, **options):
        fetcher = NewsFetcher()
        news_data = fetcher.fetch_news_from_api()
        
        if news_data:
            saved_count = fetcher.parse_and_save_news(news_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully saved {saved_count} new articles')
            )
        else:
            self.stdout.write(
                self.style.ERROR('Failed to fetch news')
            )
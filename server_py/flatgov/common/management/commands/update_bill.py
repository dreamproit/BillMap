from django.core.management.base import BaseCommand

from common import constants
from uscongress.handlers import govinfo, bills


GOVINFO_OPTIONS = {
    'collections': 'BILLS',
    'bulkdata': 'BILLSTATUS',
    'extract': 'mods,xml,premis',
}

CONGRESSES = [str(constants.CURRENT_CONGRESS)]

BILLS_OPTIONS = {
    'congress': str(constants.CURRENT_CONGRESS),
}


class Command(BaseCommand):
    help = '''update bill text and metadata by using uscongress open source scraper'''

    def handle(self, *args, **options):
        for congress in CONGRESSES:
            GOVINFO_OPTIONS['congress'] = congress
            govinfo.run(GOVINFO_OPTIONS)
            processed = bills.run(BILLS_OPTIONS)

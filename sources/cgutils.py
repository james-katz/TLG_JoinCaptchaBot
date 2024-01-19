# -*- coding: utf-8 -*-

'''
Script:
    cgutils.py
Description:
    Coingecko useful functions.
Author:
    James Katz
Creation date:
    01/15/2024
Last modified date:
    01/15/2024
Version:
    1.0
'''
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def cg_init(log):
    '''Initialize Coingecko API.'''
    log.info("Initializing coingecko API ... ")

def cg_ping():
    '''Ping coingecko servers.'''
    res = cg.ping()
    if res:
        return True
    else:
        return False

def cg_get_zec_price():
    '''Retrieve ZCASH (ZEC) current price.'''
    res = cg.get_price(ids='zcash', vs_currencies='usd')
    if(res['zcash']):
        return res['zcash']['usd']
    else:
        return -1
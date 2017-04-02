# !/usr/bin/python
# -*- coding: utf-8 -*-

# PythonCdiscount  Copyright (C) 2017    William Gerald Blondel
# contact@williamblondel.fr
# Last modified 2nd April 2017 12.56pm

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "William Gerald Blondel <contact@williamblondel.fr>"
__version__ = "0.3.5"

try:
    import requests
except ImportError:
    raise Exception("PyDiscount requires the Requests library to work. http://docs.python-requests.org/")


class PyCdiscountJobsError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class PyCdiscount:
    @staticmethod
    def __checkResponse(r):
        if r.status_code == 500:
            raise PyCdiscountJobsError(r.reason)
        elif r.status_code != 200:
            raise PyCdiscountJobsError(r.json()['Reason']['Text'])
        else:
            return r.json()

    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, keyword, sortby="relevance", itemsperpage=10, pagenumber=0, pricemin=0, pricemax=0, category="all",
               marketplace=True, brands=None, condition="all"):
        if brands is None:
            brands = []

        query = {
            'ApiKey': self.api_key,

            'SearchRequest': {
                'Keyword': keyword,
                'SortBy': sortby,
                'Pagination': {
                    'ItemsPerPage': itemsperpage,
                    'PageNumber': pagenumber
                },
                'Filters': {
                    'Price': {
                        'Min': pricemin,
                        'Max': pricemax,
                    },
                    'Navigation': category,
                    'IncludeMarketPlace': marketplace,
                    'Brands': brands,
                    'Condition': condition
                }
            }
        }

        relatedURL = "https://api.cdiscount.com/OpenApi/json/Search"

        # Do the HTTP post request
        r = requests.post(relatedURL, json=query)

        return self.__checkResponse(r)

    def getproduct(self, productid_list=None, ean_list=None, offers=True, associated_products=False, images=True,
                   ean=True):
        if ean_list is None:
            ean_list = []
        if productid_list is None:
            productid_list = []

        query = {
            'ApiKey': self.api_key,

            'ProductRequest': {
                'ProductIdList': productid_list,
                'EANList': ean_list,
                'Scope': {
                    'Offers': offers,
                    'AssociatedProducts': associated_products,
                    'Images': images,
                    'Ean': ean
                }
            }
        }

        relatedURL = "https://api.cdiscount.com/OpenApi/json/GetProduct"

        # Do the HTTP post request
        r = requests.post(relatedURL, json=query)

        return self.__checkResponse(r)

    def pushtocart(self, offerid, productid, quantity, sellerid, sizeid=None, cart_guid=None):
        query = {
            'ApiKey': self.api_key,

            'PushToCartRequest': {
                'CartGUID': cart_guid,
                'OfferId': offerid,
                'ProductId': productid,
                'Quantity': quantity,
                'SellerId': sellerid,
                'SizeId': sizeid
            }
        }

        relatedURL = "https://api.cdiscount.com/OpenApi/json/PushToCart"

        # Do the HTTP post request
        r = requests.post(relatedURL, json=query)

        return self.__checkResponse(r)

    def getcart(self, cart_guid):
        query = {
            'ApiKey': self.api_key,

            'CartRequest': {
                'CartGUID': cart_guid
            }
        }

        relatedURL = "https://api.cdiscount.com/OpenApi/json/GetCart"

        # Do the HTTP post request
        r = requests.post(relatedURL, json=query)

        return self.__checkResponse(r)

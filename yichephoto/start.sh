#!/bin/bash
rm -rf quotes.json
clear
scrapy crawl yiche -o quotes.json
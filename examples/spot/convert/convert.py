#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from binance.spot import Spot
from binance.lib.utils import config_logging
from datetime import datetime
from configparser import ConfigParser

config = ConfigParser()
config.read("../../config.ini")

config_logging(logging, logging.DEBUG)

api_key = config["keys"]["api_key"]
api_secret = config["keys"]["api_secret"]

spot_client = Spot(api_key, api_secret)

# datetime uses POSIX timestamp
start = int(datetime(2021, 11, 15, 23, 59, 59).timestamp() * 1000)
end = int(datetime(2021, 12, 7, 23, 59, 59).timestamp() * 1000)

converts = spot_client.convert_trade_history(startTime=start, endTime=end)

logging.info(converts)

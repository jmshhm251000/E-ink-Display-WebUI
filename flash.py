#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  flash.py
#  
#  Copyright 2025  <minseok@mypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import logging
import sys
import os
from epd.epd7in3f import EPD
import time
from PIL import Image
import traceback


logging.basicConfig(level=logging.info)


def main(args):
    try:
        logging.info("initiating an image display on e-ink display")
        
        bmp_path = args
        
        if not os.path.exists(bmp_path):
            raise FileNotFoundError(f"BMP file not found: {bmp_path}")
            
        epd = EPD()
        logging.info("initializing and clearing display")
        epd.init()
        epd.Clear()
        
        image = Image.open(bmp_path)
        epd.display(epd.getbuffer(image))
        time.sleep(3)
        
        logging.info("Display Going to Sleep")
        
    except IOError as e:
        logging.error("IOError:", exc_info=e)
        
    except KeyboardInterrupt:
        logging.info("ctrl + c")
        
    finally:
        try:
            from epd.epd7in3f import epdconfig
            epdconfig.module_exit(cleanup=True)
        except Exception as e:
            logging.warning("Failed to cleanup hardware:", exc_info=e)
            
        logging.shutdown()
        

if __name__ == '__main__':
    main(sys.argv[1])

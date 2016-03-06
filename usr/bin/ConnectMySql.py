#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector 

conn = mysql.connector.connect(host="localhost",user="root",password="Crepitus2015", database="test1")
cursor = conn.cursor()
conn.close()

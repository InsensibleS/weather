import datetime
import glob
import json
from time import time
import pandas as pd
import aiohttp
import requests
from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
import asyncio
from fake_useragent import UserAgent
from rest_framework.response import Response

from .models import City


class Weather(APIView):

    def get(self, request):
        query_params = self.request.query_params
        city = query_params.get('city', None)
        asyncio.run(self.get_or_create_city(city=city))
        return Response(city)

    async def get_or_create_city(self, city):
        tasks = []

        async with aiohttp.ClientSession() as session:
            for i in ['2021-12-15', '2021-12-16', '2021-12-17', '2021-12-18', '2021-12-19']:
                url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e584544aaa668cfad05097271fd37bcf&mode=json&cnt={i}"
                print(url)
                task = asyncio.create_task(self.fetch_content(url=url, session=session))
                tasks.append(task)
            await asyncio.gather(*tasks)

    async def fetch_content(self, url, session):
        async with session.get(url) as response:
            data = await response.json()
            self.write_result(data=data)

    def write_result(self, data):
        filename = 'jsons/file{}.json'.format(int(time() * 1000))
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .apps import *
import pandas as pd
import xlsxwriter

#kmeans personality prediction view
class PersonalityPrediction(APIView):
    def post(self, request):
        #get user input
        EXT1 = request.data.get('EXT1')
        EXT2 = request.data.get('EXT2')
        EXT3 = request.data.get('EXT3')
        EXT4 = request.data.get('EXT4')
        EXT5 = request.data.get('EXT5')
        EXT6 = request.data.get('EXT6')
        EXT7 = request.data.get('EXT7')
        EXT8 = request.data.get('EXT8')
        EXT9 = request.data.get('EXT9')
        EXT10 = request.data.get('EXT10')

        EST1 = request.data.get('EST1')
        EST2 = request.data.get('EST2')
        EST3 = request.data.get('EST3')
        EST4 = request.data.get('EST4')
        EST5 = request.data.get('EST5')
        EST6 = request.data.get('EST6')
        EST7 = request.data.get('EST7')
        EST8 = request.data.get('EST8')
        EST9 = request.data.get('EST9')
        EST10 = request.data.get('EST10')

        AGR1 = request.data.get('AGR1')
        AGR2 = request.data.get('AGR2')
        AGR3 = request.data.get('AGR3')
        AGR4 = request.data.get('AGR4')
        AGR5 = request.data.get('AGR5')
        AGR6 = request.data.get('AGR6')
        AGR7 = request.data.get('AGR7')
        AGR8 = request.data.get('AGR8')
        AGR9 = request.data.get('AGR9')
        AGR10 = request.data.get('AGR10')

        CSN1 = request.data.get('CSN1')
        CSN2 = request.data.get('CSN2')
        CSN3 = request.data.get('CSN3')
        CSN4 = request.data.get('CSN4')
        CSN5 = request.data.get('CSN5')
        CSN6 = request.data.get('CSN6')
        CSN7 = request.data.get('CSN7')
        CSN8 = request.data.get('CSN8')
        CSN9 = request.data.get('CSN9')
        CSN10 = request.data.get('CSN10')

        OPN1 = request.data.get('OPN1')
        OPN2 = request.data.get('OPN2')
        OPN3 = request.data.get('OPN3')
        OPN4 = request.data.get('OPN4')
        OPN5 = request.data.get('OPN5')
        OPN6 = request.data.get('OPN6')
        OPN7 = request.data.get('OPN7')
        OPN8 = request.data.get('OPN8')
        OPN9 = request.data.get('OPN9')
        OPN10 = request.data.get('OPN10')
        
        #load model
        kmeansModel = PersonalityConfig.model
        # Predicting the Clusters
        pd.options.display.max_columns = 10
        predictions = kmeansModel.labels_

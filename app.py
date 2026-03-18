from flask import Flask,render_template,request
import os
import numpy as np
import pandas as pd
from src.First_End_to_End_Project.pipeline.prediction_pipeline import PredictionPipeline

app=Flask(__name__)

@app.route('/',methods=["GET"])
def homepage():
    return render_template("index.html")
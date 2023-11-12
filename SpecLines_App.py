import streamlit as st
import pandas as pd
import numpy as np
from joblib import dump, load

st.title("Automatic Classification of Atomic Spectral Lines")
st.subheader("Version 1.0")

joblibFile = "model.joblib"

model = load(joblibFile)

#####################defs here#######################

def getUserImput():
    st.write("Please enter as much information as possible")
    obsWlVac = st.number_input("Enter the Observed Wavelength Vacuum ('obs_wl_vac(nm)'). If unknown, enter ritz wavelength:")
    ritzWlVac = st.number_input("Enter the Ritz Wavelength Vacuum ('ritz_wl_vac(nm)'). If unknown, enter observed wavelength:")
    wn = st.number_input("Enter the Wavenumber ('wn(cm-1)'). Reciprical of the wavelength:")
    aki = st.number_input("Enter the Transition Probability in 10^8s^-1 ('Aki(s^-1)'). If unknown, enter 0:")
    fik = st.number_input("Enter the Oscillator Strength ('fik'). If unknown, enter 0:")
    Sau = st.number_input("Enter the Line Strength in a.u. ('S(a.u.)'). If unknown, enter 0:")
    log_gf = st.number_input("Enter the Log of the Product of Statistical Weight and Oscillator Strength ('log_gf'). If unknown, enter 0:")
    ei = st.number_input("Enter the Interaction Energy ('Ei(cm-1)'). If unknown, enter 0:")
    ek = st.number_input("Enter the Kinetic Energy ('Ek(cm-1)'). If unknown, enter 0:")
    imputFeatures = [[obsWlVac, ritzWlVac, wn, aki, fik, Sau, log_gf, ei, ek]]
    return imputFeatures

def makePrediction(model, imput):
    return model.predict(imput)

def getPredictionElement(prediction, imput):
    elementKey = ['Helium', 'Lithium', 'Beryllium', 'Boron', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Krypton', 'Calcium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Bromine', 'Iodine']
    for i in range(len(elementKey)):
        if i == prediction:
            element = elementKey[i]
    if imputList != [[0, 0, 0, 0, 0, 0, 0, 0, 0]]:
        st.subheader("Prediction: " + element)

#####################show stuffs######################

imputList = getUserImput()
pred = makePrediction(model, imputList)
getPredictionElement(pred, imputList)
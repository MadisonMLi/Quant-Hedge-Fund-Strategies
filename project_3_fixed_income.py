# -*- coding: utf-8 -*-
"""Project_3_Fixed Income.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vVP3YlE9r2NtutykoifdyIp3yWsida9Z

## FM5422 Project 5

## Feb 22 2023
"""

!pip install QuantLib

import numpy as np
import QuantLib as ql
import pandas as pd
import statsmodels.api as sm

data = pd.read_excel("Treasury Curve Data FM 5422.xlsx")
data
yields2 = data.iloc[0]
yields2 = yields2.iloc[1:]
yields2

yields = [0]
for i in data.iloc[1249,1:]:
    yields.append(i/100)

yields

"""## Step 1. Construct 4 'Butterfly' portfolios

#### Read the data

data = pd.read_excel("Treasury Curve Data.xlsx")
data

#### Use the Feb-15-2023 yield curve to price the bonds

#### Use the QuantLib `ZeroCurve` function to bootstrap the yield curve.
"""

todaysDate = ql.Date(31, 1, 2022)
ql.Settings.instance().evaluationDate = todaysDate
Dates = [ql.Date(31, 1, 2022), ql.Date(30, 4, 2022), ql.Date(31, 7, 2022), ql.Date(31, 1, 2023), ql.Date(31, 1, 2024),ql.Date(31, 1, 2025), ql.Date(31, 1, 2027),ql.Date(31, 1, 2029), ql.Date(31, 1, 2032),ql.Date(31, 1, 2052)]

dayCount = ql.Thirty360(ql.Thirty360.BondBasis)
calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
# dayCount = ql.Thirty360()
# calendar = ql.UnitedStates()
interpolation = ql.Linear()
compounding = ql.Compounded
compoundingFrequency = ql.Annual
spotCurve = ql.ZeroCurve(Dates, yields, dayCount, calendar, interpolation,
                        compounding, compoundingFrequency)
spotCurveHandle = ql.YieldTermStructureHandle(spotCurve)

"""### 2Y bond price

#### set up the variables to price the 2Y bond.
"""

issueDate = ql.Date(31, 1, 2022)
maturityDate = ql.Date(31, 1, 2024)
tenor = ql.Period(ql.Semiannual)
calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
# calendar = ql.UnitedStates()
bussinessConvention = ql.Unadjusted
dateGeneration = ql.DateGeneration.Backward
monthEnd = False
schedule = ql.Schedule (issueDate, maturityDate, tenor, calendar, bussinessConvention,
                        bussinessConvention , dateGeneration, monthEnd)
list(schedule)

# Now lets build the coupon
dayCount = ql.Thirty360(ql.Thirty360.BondBasis)
couponRate = 0.00875
coupons = [couponRate]

# Now lets construct the FixedRateBond
settlementDays = 0
faceValue = 100
fixedRateBond = ql.FixedRateBond(settlementDays, faceValue, schedule, coupons, dayCount)

# create a bond engine with the term structure as input;
# set the bond to use this bond engine
bondEngine = ql.DiscountingBondEngine(spotCurveHandle)
fixedRateBond.setPricingEngine(bondEngine)

# Finally the price
fixedRateBond.NPV()

P_2y = fixedRateBond.NPV()

targetPrice = fixedRateBond.cleanPrice()
day_count = dayCount
compounding = ql.Compounded
frequency = 2
ytm = fixedRateBond.bondYield(targetPrice, day_count, compounding, frequency)
# print(ytm)
rate = ql.InterestRate(ytm, ql.ActualActual(ql.ActualActual.Bond), ql.Compounded, ql.Annual)
mod_2y = ql.BondFunctions.duration(fixedRateBond,rate,ql.Duration.Modified)
mod_2y

"""### Calcualte 5Y Bond Price"""

issueDate = ql.Date(31, 1, 2023)
maturityDate = ql.Date(31, 1, 2028)
tenor = ql.Period(ql.Semiannual)
calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
bussinessConvention = ql.Unadjusted
dateGeneration = ql.DateGeneration.Backward
monthEnd = False
schedule = ql.Schedule (issueDate, maturityDate, tenor, calendar, bussinessConvention,
                        bussinessConvention , dateGeneration, monthEnd)
list(schedule)
# Now lets build the coupon
dayCount = ql.Thirty360(ql.Thirty360.BondBasis)
couponRate = 0.035
coupons = [couponRate]

# Now lets construct the FixedRateBond
settlementDays = 0
faceValue = 100
fixedRateBond = ql.FixedRateBond(settlementDays, faceValue, schedule, coupons, dayCount)

# create a bond engine with the term structure as input;
# set the bond to use this bond engine
bondEngine = ql.DiscountingBondEngine(spotCurveHandle)
fixedRateBond.setPricingEngine(bondEngine)

# Finally the price
fixedRateBond.NPV()
P_5y = fixedRateBond.NPV()
targetPrice = fixedRateBond.cleanPrice()
day_count = dayCount
compounding = ql.Compounded
frequency = 2
ytm = fixedRateBond.bondYield(targetPrice, day_count, compounding, frequency)
# print(ytm)
rate = ql.InterestRate(ytm, ql.ActualActual(ql.ActualActual.Bond), ql.Compounded, ql.Annual)
mod_5y = ql.BondFunctions.duration(fixedRateBond,rate,ql.Duration.Modified)
mod_5y

"""#### Same procedure here, pricing the 5Y bond, we'll skip the comments

### Calculate 10Y Bond Price
"""

issueDate = ql.Date(31, 1, 2023)
maturityDate = ql.Date(31, 1, 2033)
tenor = ql.Period(ql.Semiannual)
calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
bussinessConvention = ql.Unadjusted
dateGeneration = ql.DateGeneration.Backward
monthEnd = False
schedule = ql.Schedule (issueDate, maturityDate, tenor, calendar, bussinessConvention,
                        bussinessConvention , dateGeneration, monthEnd)
list(schedule)
# Now lets build the coupon
dayCount = ql.Thirty360(ql.Thirty360.BondBasis)
couponRate = 0.035
coupons = [couponRate]

# Now lets construct the FixedRateBond
settlementDays = 0
faceValue = 100
fixedRateBond = ql.FixedRateBond(settlementDays, faceValue, schedule, coupons, dayCount)

# create a bond engine with the term structure as input;
# set the bond to use this bond engine
bondEngine = ql.DiscountingBondEngine(spotCurveHandle)
fixedRateBond.setPricingEngine(bondEngine)

# Finally the price
fixedRateBond.NPV()
P_10y = fixedRateBond.NPV()

targetPrice = fixedRateBond.cleanPrice()
day_count = dayCount
compounding = ql.Compounded
frequency = 2
ytm = fixedRateBond.bondYield(targetPrice, day_count, compounding, frequency)
# print(ytm)
rate = ql.InterestRate(ytm, ql.ActualActual(ql.ActualActual.Bond), ql.Compounded, ql.Annual)
mod_10y = ql.BondFunctions.duration(fixedRateBond,rate,ql.Duration.Modified)
mod_10y

"""<br>

### Now, we calcuate the dollar duration and duration of each bond and use them to construct the butterflies.

####  But, first we need to calculate the beta in strategy 3.

"""

Y_10 = data.iloc[:,-2]
Y_5 = data.iloc[:,-4]
Y_2 = data.iloc[:,4]
Y10_5 = Y_10 - Y_5
Y5_2 = Y_5 - Y_2

"""Getting the changes on two sides"""

x = Y10_5.diff().dropna()#[-65:] if 3 month
x

y = Y5_2.diff().dropna()#[-65:]
y

"""Fitting regression"""

x = sm.add_constant(x)
lm = sm.OLS(y,x).fit()
lm.summary()

beta = lm.params[0]

dol_2y = .01**2*mod_2y*P_2y*10000
dol_5y = .01**2*mod_5y*P_5y*10000
dol_10y = .01**2*mod_10y*P_10y*10000

beta

lm.summary()

beta

"""<br>


### Constructing 4 butterflies portfolio

#### The cash-and $duration neutral weighting butterfly
"""

from sympy import symbols, Eq, solve

# defining symbols used in equations
# or unknown variables
x1, qu = symbols('x1,qu')

# defining equations
eq1 = Eq(x1*dol_2y+qu*dol_10y+100*dol_5y,0)
print("Equation 1:")
print(eq1)
eq2 = Eq(x1*P_2y+qu*P_10y+100*P_5y,0)
print("Equation 2")
print(eq2)

# solving the equation
print("Values of 2 unknown variable are as follows:")

print(solve((eq1, eq2), (x1, qu)))

x1 = -58
qu = -41

x1*dol_2y+qu*dol_10y-100*dol_5y

cash_dur_nut = [x1,qu]
cash_dur_nut



"""#### The fifty-fifty weighting regression"""

# defining symbols used in equations
# or unknown variables
x1, qu ,alpha= symbols('x1,qu,alpha')

# defining equations

eq2 = Eq(x1*dol_2y + 100*dol_5y/2,0)
print("Equation 2")
print(eq2)
eq3 = Eq(qu*dol_10y + 100*dol_5y/2, 0)
print("Equation 3")
print(eq3)
#eq3 = Eq(qu*dol_10y+alpha*dol_5y,0)

# solving the equation
print("Values of 2 unknown variable are as follows:")

print(solve((eq2, eq3), (x1, qu)))

x1 = -118
qu = -27
fifty_wight_reg = [x1,qu]
fifty_wight_reg

"""#### Regression Weighting Butterfly"""

# defining symbols used in equations
# or unknown variables
x1, qu ,alpha= symbols('x1,qu,alpha')

# defining equations
eq1 = Eq(x1*dol_2y+qu*dol_10y+100*dol_5y,0)
print("Equation 1:")
print(eq1)
eq2 = Eq(x1*dol_2y*(1/beta)-qu*dol_10y,0)
print("Equation 2")
print(eq2)

#eq3 = Eq(qu*dol_10y+alpha*dol_5y,0)

# solving the equation
print("Values of 2 unknown variable are as follows:")

print(solve((eq1, eq2), (x1, qu)))

x1 = -77
qu = -37

x1*dol_2y*(1/beta)-qu*dol_10y

reg_wei_reg = [x1,qu]
reg_wei_reg

"""#### Maturity-Weighting Butterfly"""

# defining symbols used in equations
# or unknown variables
x1, qu ,alpha= symbols('x1,qu,alpha')

M1 = (5-2)/(10-2)
M2 = (10-5)/(10-2)

# defining equations
eq3 = Eq(x1*dol_2y+qu*dol_10y+100*dol_5y,0)
print("Equation 1:")
print(eq1)
eq1 = Eq(x1*dol_2y+100*M1*dol_5y,0)
eq2 = Eq(qu*dol_10y+100*M2*dol_5y,0)
print("Equation 2")
print(eq2)

#eq3 = Eq(qu*dol_10y+alpha*dol_5y,0)

# solving the equation
print("Values of 2 unknown variable are as follows:")

print(solve((eq1, eq2,eq3), (x1, qu)))

x1 = -89
qu = -34

mat_wei_reg = [x1,qu]
mat_wei_reg

"""<br>


## Step 2. PCA curves

Calculate daily treasury shifts and standardize data

diff = data.diff().dropna().iloc[:,1:]
diff = (diff - diff.mean()) / diff.std()

covs = np.cov(np.array(np.array(diff)).T)
covs

eigs, eigvecs = np.linalg.eig(covs)
eigs
"""

diff = data.diff().dropna().iloc[:,1:]
diff = (diff - diff.mean()) / diff.std()
covs = np.cov(np.array(np.array(diff)).T)
covs
eigs, eigvecs = np.linalg.eig(covs)
eigs

eigvecs[:,0]

np.shape(eigvecs)

import matplotlib.pyplot as plt
plt.figure(figsize=(15,10))
for i in range(3):
    if i == 1:
        plt.plot(-eigvecs[:,i], label = 'PC_'+str(i+1))
    else:
        plt.plot(eigvecs[:,i], label = 'PC_'+str(i+1))

plt.legend()
plt.show()

"""<br>

## Step 3. Apply changes to PCA for the 3 Scenatios
"""

a1 = 0.0005/eigvecs[-2, 0]
a1

a2 = 0.0005/-(eigvecs[-2,1] - eigvecs[3,1])
a2

a3 = 0.0005/(2* eigvecs[5,2] - eigvecs[-2,2] - eigvecs[3,2])
a3

pc1_scale_yields = [0]
pc2_scale_yields = [0]
pc3_scale_yields = [0]

for i in range (len(yields)-1):
    pc1_scale_yields += [a1 * eigvecs[i,0] + yields[i+1]]
    pc2_scale_yields += [a2 * eigvecs[i,1] + yields[i+1]]
    pc3_scale_yields += [a3 * eigvecs[i,2] + yields[i+1]]
pc1_scale_yields,pc2_scale_yields,pc3_scale_yields

"""## Step 4 Calculate individual bonds Prices under the 3 scenarios"""

ql

def bond_price (yields, coupon, maturity_year):
    todaysDate = ql.Date(31, 1, 2023)
    ql.Settings.instance().evaluationDate = todaysDate
    Dates = [ql.Date(31, 1, 2023), ql.Date(30, 4, 2023), ql.Date(31, 7, 2023), ql.Date(31, 1, 2024), ql.Date(31, 1, 2025),ql.Date(31, 1, 2026), ql.Date(31, 1, 2028),ql.Date(31, 1, 2030), ql.Date(31, 1, 2033),ql.Date(31, 1, 2053)]

    dayCount = ql.Thirty360(ql.Thirty360.BondBasis)
    calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
    interpolation = ql.Linear()
    compounding = ql.Compounded
    compoundingFrequency = ql.Annual
    spotCurve = ql.ZeroCurve(Dates, yields, dayCount, calendar, interpolation,
                            compounding, compoundingFrequency)
    spotCurveHandle = ql.YieldTermStructureHandle(spotCurve)
    issueDate = ql.Date(31, 1, 2023)
    maturityDate = ql.Date(31, 1, maturity_year)
    tenor = ql.Period(ql.Semiannual)
    calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
    bussinessConvention = ql.Unadjusted
    dateGeneration = ql.DateGeneration.Backward
    monthEnd = False
    schedule = ql.Schedule (issueDate, maturityDate, tenor, calendar, bussinessConvention,
                            bussinessConvention , dateGeneration, monthEnd)

    dayCount = ql.Thirty360(ql.Thirty360.BondBasis)
    couponRate = coupon
    coupons = [couponRate]
    settlementDays = 0
    faceValue = 100
    fixedRateBond = ql.FixedRateBond(settlementDays, faceValue, schedule, coupons, dayCount)
    bondEngine = ql.DiscountingBondEngine(spotCurveHandle)
    fixedRateBond.setPricingEngine(bondEngine)
    return (fixedRateBond.NPV())

yields_list = [pc1_scale_yields, pc2_scale_yields, pc3_scale_yields]
maturies = [2025, 2028, 2033]
coupons_rate = [0.04125, 0.035, 0.035]
prices = np.ones((3,3))
for i in range(len(yields_list)):
    for j in range(len(coupons_rate)):
        prices [i,j] = bond_price(yields_list[i], coupons_rate[j], maturies[j])
prices

old_price =  [P_2y, P_5y, P_10y]
old_price

positions = [cash_dur_nut, fifty_wight_reg, reg_wei_reg, mat_wei_reg]
positions

"""## Step 5 Calculate the pnl for each of the butterfly portfolios under the 3 scenarios"""

pnl = np.zeros((3,4))
for i in range(len(prices)):
    for j in range(len(positions)):
        pnl[i,j] = positions[j][0]*(prices[i][0] - old_price[0]) + 100*( prices[i][1]- old_price[1]) + positions[j][1]*( prices[i][2]- old_price[2])
pnl

scenarios = ['a1', 'a2','a3']
for i in range(len(scenarios)):
    print("Cash and Dollar duration butterfly pnl for " + scenarios[i] + " is ", pnl[i][0])
    print("Fifty-Fifty weighting butterfly pnl for " + scenarios[i] + " is ", pnl[i][1])
    print("Regression weighting butterfly pnl for " + scenarios[i] + " is ", pnl[i][2])
    print("Maturity weighting butterfly pnl for " + scenarios[i] + " is " , pnl[i][3])
    print()
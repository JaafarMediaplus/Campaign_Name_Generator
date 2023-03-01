from math import prod
from platform import platform
import streamlit as st
import pandas as pd
import numpy as np


st.title('Campaign Name Generator')

st.title("")

# BEGINNING OF SECTION 1 ///

# Phase
phase = st.selectbox(
    'Campaign Phase:',
    ('NA', 'AWRNS', 'TRFC', 'CONV', 'APP')
)

st.title('')

# brand and subbrand
colbrand, colsubbrand = st.columns(2)
brand = colbrand.selectbox(
     'Brand Title:',
     ('NA', 'RT', 'Dabur', 'Abbott', 'CapriSun', 'BS', 'FS', 'Twnenty4', 
     'ALJUF', 'Midea', 'OQ', 'MAMC', 'UBF')
     )
sub_brand = colsubbrand.selectbox(
    'Sub-Brand Title:',
    ('NA', 'AlwaysOn', 'SME', 'Auto', 'CashIndividual', 'UsedCars', 'LunarDialSeries', 'FSL', 'ALJapp',
     'Fleet',  'Forklift', 'FSLGeofence')
    )

# Region and market
colregion, colmarket = st.columns(2)
region = colregion.selectbox(
    'Target Region:',
    ('NA', 'Multiple', 'GCC', 'MENA', 'Egypt', 'KSA', 'UAE', 'Generic', 'Cities', 'Jeddah')
)
market = colmarket.selectbox(
    'Target Market:',
    ('NA', 'RoGCC', 'UAE', 'KSA', 'KW', 'QA', 'BH', 'OM', 'EG', 'ALG', 'MOROC', 'LBYA', 
     'YMN', 'IRQ', 'JRDN', 'LEB', 'KAZAKH', 'PKSTN', 'IND', 'RSNSPKCNT', 'SPN', 'TRKY', 'VTNM', 'Jeddah')
)

# store and area
colstore, colarea = st.columns(2)
store = colstore.selectbox(
    'Store Name:',
    ('NA', 'AlNahdiR1', 'AlNahdiR2', 'Innova', 'AlDawaaR1', 'AlDawaaR2', 'AlNahdiJ1', 'AlNahdiJ2', 'AlNahdiJ3', 'AlDawaaJ1', 'AlDawaaE1', 'AlNahdiE1', 
    'AlDawaaE2', 'SAHR1', 'SAHR2', 'SAHR3', 'SAHR4', 'DallahK1', 'SAHK1', 'AlmanaK1', 'MouwasatK1', 'MouwasatJU1', 'SAHQ1', 'IMCHJeddah', 'SFHJeddah')
)
area = colarea.selectbox(
    'Target Area:',
    ('NA', 'Dubai', 'AbuDhabi', 'Riyadh', 'Jeddah',  'Hospitals', 'RiyadhHospitals', 'KhobarHospitals', 'JeddahHospitals', 'BuraydahBranchQasim', 
    'Jubail', 'Pharmacies', 'RiyadhPharmacies', 'JeddahPharmacies', 'EasternRegionPharmacies')
)

# buy type and targeting
colbuytype, coltargeting = st.columns(2)
buytype = colbuytype.selectbox(
    'Campaign Buy Type:',
    ('NA', 'CPMR', 'CPM', 'CPC', 'CPV', 'CPL', 'CPA', 'CPLPV', 'RMKT', 'CPE', 'RnF', 'RnFEn', 'RnFAr', 'CPSU')
)
targeting = coltargeting.selectbox(
    'Audience Targeting:',
    ('NA', 'INTR', 'GEO', 'RMKT', 'Custom', 'Affinity', 'CustomAffinity', 'Custom&LookAlikes', 
    'InMarketAudience', 'AffinityAudience', 'SimilarToLeads', 'BusinessPlacement', 'Multiple', 'RLSA', 'SimilarAudience', 'WBSTVisitors', 'SMLRtoWBSTVisitors', 'Topic',
    'SMLRWebt&Apps', 'Auto', 'Keyword')
)

# placement (platform) and special offer
colplacement, colspecialoffer = st.columns(2)
placement = colplacement.selectbox(
    'Advertising Media Platform:',
    ('NA', 'FBIG', 'IG', 'FB', 'GDN', 'SRCH', 'YT', 'SNAP', 
    'TT', 'LNKDI', 'YHO', 'SPKL', 'TDS', 'AMZN', 'DSCVRY', 'TWT', 'Nabd', 'Quora', 'GUAC', 'PMN', 'SrchAds', 'MaxPerf', 'Upswiit')
)
special_offer = colspecialoffer.selectbox(
    'Special Offer Title:',
    ('NA', 'Contextual', 'FreeBHD3', 'SpecialOffer', 'RamadanWrapUp', 'Testimonial', 'Buy2Get1Free', 'LastDays', 'NationalDay', 'ClickButton', 'Ramadan')
)



st.title('')

# product and product variant / Creative name
colproduct, colproductvariant = st.columns(2)
product = colproduct.selectbox(
    'Product Name:',
    ('NA', 'All', 'WashingMachine', 'System', 'CRM', 'Dueler', 'Potenza', 'Alenza', 'Ecopia', 'ContentHub', 'UGC', 'SME', 'Auto',
     'Polyethylene', 'Polypropylene', 'FoodPackaging', 'SME', 'Toyota', 'Kia', 'Hyundai', 'Geely', 'CashIndividual', 'UsedCars', 'DistractedDriving', 'ClearRoad',
    'RealEstate', 'Microfinance', 'TodayTab', 'SrchTab', 'SrchResults', 'ProductPage', 'app', 'Excellence', 'Stars')
)
product_variant = colproductvariant.selectbox(
    'Product Variant/Creative Name:',
    ('NA', 'SME', 'Auto', 'Archi', 'Tech', 'Artist', 'KV1', 'KV2', 'KV3', 'ArchiKV2', 'TechKV3', 'ArtistKV1', 'Toyota', 'Kia', 'Hyundai', 'Geely', 'CashIndividual', 'UsedCars', 'Suzuki', 
     'SustainableDriving', 'Destination', 'OnOffRoad', 'EngineNoises', 'PotenzaSport', 'SilenceIsGolden', 'UGC', 'AugustPost6', 'AugustPost7',
     'SeptCarousel', 'AugCarousel', 'SeptHTML5', 'PostRamadanVideo', ' SepPost2', 'SepPost3', 'SepPost4', 'SepPost5' , 'SeptPost6', 'SepPost7', 'SepPost8', 
    'CRMCarousel', 'SystemCarousel', '999Offer', 'TyreWear', 'Breathtaking', ' EngineeredToImpress', 'ReadyForTakeOff', 'PerfectModel', 'ReadyForWherever', 'OffRoad',
    'WobblingTyre', 'TyreWear', 'FatherSon', 'MotherSon', '28Sec', '57Sec', '15Sec', 'MotherSon&FatherSon', 'DistractedDriving', 'ClearRoad', 'PotenzaSport', 'Maserati',
    'RealEstate', 'Microfinance', 'Smooth&BaldTyres', 'IjarahHome', 'IjarahLand', 'BuildingCompletionSME', 'Sale&LeaseBack', 'Kia1', 'Kia2', 'LongLasting',
    'Product1', 'Product2', 'Product3', 'Product4', 'Tactical', '15mill', 'AutumnPlaylist', '15secCTA', '15sec', '46sec', 'TamakanSME', 'Dependability', 'PerformancePower',
    'Fleet', 'Forklift', 'Emergency', 'Cold', 'RPM', 'Historical', 'Video1', 'Video2', 'Video3', 'Video4', 'Carousel1', 'Carousel2', 'BannerMan', 'BannerWoman')
)

# language and gender
collanguage, colgender = st.columns(2)
language = collanguage.selectbox(
    'Target Language:',
    ('NA', 'En', 'Ar', 'EnAr')
)
gender = colgender.selectbox(
    'Target Gender:',
    ('NA', 'M', 'F', 'MF')
)

# age and format
colage, colformat = st.columns(2)
age = colage.selectbox(
    'Target Age:',
    ('NA', '18to24', '25to34', '18to54', '18to50', '24+')
)
format = colformat.selectbox(
    'Ad Format:',
    ('NA', 'Native', 'StaticImage', 'Video', 'Carousel', 'Catalog', 'Responsive', 
    'Expended', 'Gmail', 'Discovery', 'HTML5', 'StaticDisplay', 'Multiple', 'DSCVRYAd', 'DSCVRYCarouselAd', 'Banner', 'SkippableAd')
)

# device
device_name = st.selectbox(
    'Device Type:',
    ('NA', 'Desktop', 'Mobile', 'iOS', 'Android')
)

# month and year
colyear, colmonth = st.columns(2)
year = colyear.selectbox(
    'Campaign Initiation Year:',
    ('NA', '22', '23')
)
month = colmonth.selectbox(
    'Campaign Initiation Month:',
    ('NA', 'Jan', 'Feb', 'Mar', 'Apr', 'May',
    'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 
    'Nov', 'Dec', 'OctNov', 'OctNovDec')
)

st.title('')

# keyword group
keyword_group = st.selectbox(
    'Keyword Group (For Google Search):',
    ('NA', 'GNRC', 'COMPT', 'BRND', 'TradeBusinessLicense', 'CompanyKeywords', 'EcommerceKeywords',
    'FreelanceKeywords', 'Brand&Generic')
)

# END OF SECTION 1 ///



# SECTION 2 ///
# Coding Scheme for campaign name elements.


# Brand Coding
if brand == 'RT':
    coded_brand = brand.replace('RT', 'B001')
elif brand == 'Dabur':
    coded_brand = brand.replace('Dabur', 'B002')
elif brand == 'Abbott':
    coded_brand = brand.replace('Abbott', 'B003')
elif brand == 'CapriSun':
    coded_brand = brand.replace('CapriSun', 'B004')
elif brand == 'BS':
    coded_brand = brand.replace('BS', 'B005')
elif brand == 'FS':
    coded_brand = brand.replace('FS', 'B006')
elif brand == 'Twenty4':
    coded_brand = brand.replace('Twenty4', 'B007')
elif brand == 'ALJUF':
    coded_brand = brand.replace('ALJUF', 'B008')
elif brand == 'Midea':
    coded_brand = brand.replace('Midea', 'B009')
elif brand == 'OQ':
    coded_brand = brand.replace('OQ', 'B010')
elif brand == 'MAMC':
    coded_brand = brand.replace('MAMC', 'B011')
elif brand == 'UBF':
    coded_brand = brand.replace('UBF', 'B012')
else:
    coded_brand = brand.replace('Null', 'B000')


# Sub-brand Coding
if sub_brand == 'AlwaysOn':
    coded_sub_brand = sub_brand.replace('AlwaysOn', 'SB001')
elif sub_brand == 'SME':
    coded_sub_brand = sub_brand.replace('SME', 'SB002')
elif sub_brand == 'Auto':
    coded_sub_brand = sub_brand.replace('Auto', 'SB003')
elif sub_brand == 'CashIndividual':
    coded_sub_brand = sub_brand.replace('CashIndividual', 'SB004')
elif sub_brand == 'UsedCars':
    coded_sub_brand = sub_brand.replace('UsedCars', 'SB005')
elif sub_brand == 'LunarDialSeries':
    coded_sub_brand = sub_brand.replace('LunarDialSeries', 'SB006')
elif sub_brand == 'FSL':
    coded_sub_brand = sub_brand.replace('FSL', 'SB007')
elif sub_brand == 'ALJapp':
    coded_sub_brand = sub_brand.replace('ALJapp', 'SB008')
elif sub_brand == 'Fleet':
    coded_sub_brand = sub_brand.replace('Fleet', 'SB009')
elif sub_brand == 'Forklift':
    coded_sub_brand = sub_brand.replace('Forklift', 'SB010')
elif sub_brand == 'FSLGeofence':
    coded_sub_brand = sub_brand.replace('FSLGeofence', 'SB011')
else:
    coded_sub_brand = sub_brand.replace('Null', 'SB0')


# Product Coding
if product == 'All':
    coded_product = product.replace('All', 'P001')
elif product == 'WashingMachine':
    coded_product = product.replace('WashingMachine', 'P002')
elif product == 'System':
    coded_product = product.replace('System', 'P003')
elif product == 'CRM':
    coded_product = product.replace('CRM', 'P004')
elif product == 'Dueler':
    coded_product = product.replace('Dueler', 'P005')
elif product == 'Potenza':
    coded_product = product.replace('Potenza', 'P006')
elif product == 'Alenza':
    coded_product = product.replace('Alenza', 'P007')
elif product == 'Ecopia':
    coded_product = product.replace('Ecopia', 'P008')
elif product == 'ContentHub':
    coded_product = product.replace('ContentHub', 'P009')
elif product == 'UGC':
    coded_product = product.replace('UGC', 'P010')
elif product == 'SME':
    coded_product = product.replace('SME', 'P011')
elif product == 'Auto':
    coded_product = product.replace('Auto', 'P012')
elif product == 'Polyethylene':
    coded_product = product.replace('Polyethylene', 'P013')
elif product == 'Polypropylene':
    coded_product = product.replace('Polypropylene', 'P014')
elif product == 'FoodPackaging':
    coded_product = product.replace('FoodPackaging', 'P015')
elif product == 'Toyota':
    coded_product = product.replace('Toyota', 'P016')
elif product == 'Kia':
    coded_product = product.replace('Kia', 'P017')
elif product == 'Hyundai':
    coded_product = product.replace('Hyundai', 'P018')
elif product == 'Geely':
    coded_product = product.replace('Geely', 'P019')
elif product == 'CashIndividual':
    coded_product = product.replace('CashIndividual', 'P020')
elif product == 'UsedCars':
    coded_product = product.replace('UsedCars', 'P021')
elif product == 'DistractedDriving':
    coded_product = product.replace('DistractedDriving', 'P022')
elif product == 'ClearRoad':
    coded_product = product.replace('ClearRoad', 'P023')
elif product == 'RealEstate':
    coded_product = product.replace('RealEstate', 'P024')
elif product == 'Microfinance':
    coded_product = product.replace('Microfinance', 'P025')
elif product == 'TodayTab':
    coded_product = product.replace('TodayTab', 'P026')
elif product == 'SrchTab':
    coded_product = product.replace('SrchTab', 'P027')
elif product == 'SrchResults':
    coded_product = product.replace('SrchResults', 'P028')
elif product == 'ProductPage':
    coded_product = product.replace('ProductPage', 'P029')
elif product == 'app':
    coded_product = product.replace('app', 'P030')
elif product == 'Excellence':
    coded_product = product.replace('TodayTab', 'P031')
elif product == 'Stars':
    coded_product = product.replace('Stars', 'P032')
else:
    coded_product = product.replace('Null', 'P000')


# Region Coding
if region == 'Multiple':
    coded_region = region.replace('Multiple', 'R001')
elif region == 'GCC':
    coded_region = region.replace('GCC', 'R002')
elif region == 'MENA':
    coded_region = region.replace('MENA', 'R003')
elif region == 'Egypt':
    coded_region = region.replace('Egypt', 'R004')
elif region == 'KSA':
    coded_region = region.replace('KSA', 'R005')
elif region == 'UAE':
    coded_region = region.replace('UAE', 'R006')
elif region == 'Generic':
    coded_region = region.replace('Generic', 'R007')
elif region == 'Cities':
    coded_region = region.replace('Cities', 'R008')
elif region == 'Jeddah':
    coded_region = region.replace('Jeddah', 'R009')
else:
    coded_region = region.replace('Null', 'R000')


# Market Coding
if market == 'RoGCC':
    coded_market = market.replace('RoGCC', 'M001')
elif market == 'UAE':
    coded_market = market.replace('UAE', 'M002')
elif market == 'KSA':
    coded_market = market.replace('KSA', 'M003')
elif market == 'KW':
    coded_market = market.replace('KW', 'M004')
elif market == 'QA':
    coded_market = market.replace('QA', 'M005')
elif market == 'BH':
    coded_market = market.replace('BH', 'M006')
elif market == 'OM':
    coded_market = market.replace('OM', 'M007')
elif market == 'EG':
    coded_market = market.replace('EG', 'M008')
elif market == 'ALG':
    coded_market = market.replace('ALG', 'MOO9')
elif market == 'MOROC':
    coded_market = market.replace('MOROC', 'M010')
elif market == 'LBYA':
    coded_market = market.replace('LBYA', 'M011')
elif market == 'YMN':
    coded_market = market.replace('YMN', 'M012')
elif market == 'IRQ':
    coded_market = market.replace('IRQ', 'M013')
elif market == 'JRDN':
    coded_market = market.replace('JRDN', 'M014')
elif market == 'LEB':
    coded_market = market.replace('LEB', 'M015')
elif market == 'KAZAKH':
    coded_market = market.replace('KAZAKH', 'M016')
elif market == 'PKSTN':
    coded_market = market.replace('PKSTN', 'M017')
elif market == 'IND':
    coded_market = market.replace('IND', 'M018')
elif market == 'RSNSPKCNT':
    coded_market = market.replace('RSNSPKCNT', 'M019')
elif market == 'SPN':
    coded_market = market.replace('SPN', 'M020')
elif market == 'TRKY':
    coded_market = market.replace('TRKY', 'M021')
elif market == 'VTNM':
    coded_market = market.replace('VTNM', 'M022')
elif market == 'Jeddah':
    coded_market = market.replace('Jeddah', 'M023')
else:
    coded_market = market.replace('Null', 'M000')


# Area Coding
if area == 'Dubai':
    coded_area = area.replace('Dubai', 'A001')
elif area == 'AbuDhabi':
    coded_area = area.replace('AbuDhabi', 'A002')
elif area == 'Riyadh':
    coded_area = area.replace('Riyadh', 'A003')
elif area == 'Jeddah':
    coded_area = area.replace('Jeddah', 'A004')
elif area == 'RiyadhHospitals':
    coded_area = area.replace('RiyadhHospitals', 'A005')
elif area == 'KhobarHospitals':
    coded_area = area.replace('KhobarHospitals', 'A006')
elif area == 'JeddahHospitals':
    coded_area = area.replace('JeddahHospitals', 'A007')
elif area == 'BuraydahBranchQasim':
    coded_area = area.replace('BuraydahBranchQasim', 'A008')
elif area == 'Jubail':
    coded_area = area.replace('Jubail', 'A009')
elif area == 'Pharmacies':
    coded_area = area.replace('Pharmacies', 'A010')
elif area == 'RiyadhPharmacies':
    coded_area = area.replace('RiyadhPharmacies', 'A011')
elif area == 'JeddahPharmacies':
    coded_area = area.replace('JeddahPharmacies', 'A012')
elif area == 'EasternRegionPharmacies':
    coded_area = area.replace('EasternRegionPharmacies', 'A013')
else:
    coded_area = area.replace('Null', 'A000')


# Store Coding
if store == 'AlNahdiR1':
    coded_area = store.replace('AlNahdiR1', 'S001')
elif store == 'AlNahdiR2':
    coded_store = store.replace('AlNahdiR2', 'S002')
elif store == 'Innova':
    coded_store = store.replace('Innova', 'S003')
elif store == 'AlDawaaR1':
    coded_store = store.replace('AlDawaaR1', 'S004')
elif store == 'AlDawaaR2':
    coded_store = store.replace('AlDawaaR2', 'S005')
elif store == 'AlNahdiJ1':
    coded_store = store.replace('AlNahdiJ1', 'S006')
elif store == 'AlNahdiJ2':
    coded_store = store.replace('AlNahdiJ2', 'S007')
elif store == 'AlNahdiJ3':
    coded_store = store.replace('AlNahdiJ3', 'S008')
elif store == 'AlDawaaJ1':
    coded_store = store.replace('AlDawaaJ1', 'S009')
elif store == 'AlDawaaE1':
    coded_store = store.replace('AlDawaaE1', 'S010')
elif store == 'AlNahdiE1':
    coded_store = store.replace('AlNahdiE1', 'S011')
elif store == 'AlDawaaE2':
    coded_store = store.replace('AlDawaaE2', 'S012')
elif store == 'SAHR1':
    coded_store = store.replace('SAHR1', 'S013')
elif store == 'SAHR2':
    coded_store = store.replace('SAHR2', 'S014')
elif store == 'SAHR3':
    coded_store = store.replace('SAHR3', 'S015')
elif store == 'SAHR4':
    coded_store = store.replace('SAHR4', 'S016')
elif store == 'DallahK1':
    coded_store = store.replace('DallahK1', 'S017')
elif store == 'SAHK1':
    coded_store = store.replace('SAHK1', 'S018')
elif store == 'AlmanaK1':
    coded_store = store.replace('AlmanaK1', 'S019')
elif store == 'MouwasatK1':
    coded_store = store.replace('MouwasatK1', 'S020')
elif store == 'MouwasatJU1':
    coded_store = store.replace('MouwasatJU1', 'S021')
elif store == 'SAHQ1':
    coded_store = store.replace('SAHQ1', 'S022')
elif store == 'IMCHJeddah':
    coded_store = store.replace('IMCHJeddah', 'S023')
elif store == 'SFHJeddah':
    coded_store = store.replace('SFHJeddah', 'S024')
else:
    coded_store = store.replace('Null', 'S000')


# Phase Coding
if phase == 'AWRNS':
    coded_phase = phase.replace('AWRNS', 'PH001')
elif phase == 'TRFC':
    coded_phase = phase.replace('TRFC', 'PH002')
elif phase == 'CONV':
    coded_phase = phase.replace('CONV', 'PH003')
elif phase == 'APP':
    coded_phase = phase.replace('APP', 'PH004')
else:
    coded_phase = phase.replace('Null', 'PH000')


# Buy Type Coding
if buytype == 'CPMR':
    coded_buytype = buytype.replace('CPMR', 'BT001')
elif buytype == 'CPC':
    coded_buytype = buytype.replace('CPC', 'BT002')
elif buytype == 'CPV':
    coded_buytype = buytype.replace('CPV', 'BT003')
elif buytype == 'CPL':
    coded_buytype = buytype.replace('CPL', 'BT004')
elif buytype == 'CPA':
    coded_buytype = buytype.replace('CPA', 'BT005')
elif buytype == 'CPLPV':
    coded_buytype = buytype.replace('CPLPV', 'BT006')
elif buytype == 'RMKT':
    coded_buytype = buytype.replace('RMKT', 'BT007')
elif buytype == 'CPE':
    coded_buytype = buytype.replace('CPE', 'BT008')
elif buytype == 'RnF':
    coded_buytype = buytype.replace('RnF', 'BT009')
elif buytype == 'RnFEn':
    coded_buytype = buytype.replace('RnFEn', 'BT010')
elif buytype == 'RnFAr':
    coded_buytype = buytype.replace('RnFAr', 'BT011')
elif buytype == 'CPSU':
    coded_buytype = buytype.replace('CPSU', 'BT012')
elif buytype == 'CPM':
    coded_buytype = buytype.replace('CPM', 'BT013')
else:
    coded_buytype = buytype.replace('Null', 'BT000')


# Special Offer Coding
if special_offer == 'Contextual':
    coded_specialoffer = special_offer.replace('Contextual', 'SO001')
elif special_offer == 'FreeBHD3':
    coded_specialoffer = special_offer.replace('FreeBHD3', 'SO002')
elif special_offer == 'SpecialOffer':
    coded_specialoffer = special_offer.replace('SpecialOffer', 'SO003')
elif special_offer == 'RamadanWrapUp':
    coded_specialoffer = special_offer.replace('RamadanWrapUp', 'SO004')
elif special_offer == 'Testimonial':
    coded_specialoffer = special_offer.replace('Testimonial', 'SO005')
elif special_offer == 'Buy2Get1Free':
    coded_specialoffer = special_offer.replace('Buy2Get1Free', 'SO006')
elif special_offer == 'LastDays':
    coded_specialoffer = special_offer.replace('LastDays', 'SO007')
elif special_offer == 'NationalDay':
    coded_specialoffer = special_offer.replace('NationalDay', 'SO008')
elif special_offer == 'ClickButton':
    coded_specialoffer = special_offer.replace('ClickButton', 'SO009')
elif special_offer == 'Ramadan':
    coded_specialoffer = special_offer.replace('Ramadan', 'SO010')
else:
    coded_specialoffer = special_offer.replace('Null', 'SO000')



# Keyword Group Coding
if keyword_group == 'GNRC':
    coded_keywordgroup = keyword_group.replace('GNRC', 'KG001')
elif keyword_group == 'COMPT':
    coded_keywordgroup = keyword_group.replace('COMPT', 'KG002')
elif keyword_group == 'BRND':
    coded_keywordgroup = keyword_group.replace('BRND', 'KG003')
elif keyword_group == 'TradeBusinessLicense':
    coded_keywordgroup = keyword_group.replace('TradeBusinessLicense', 'KG004')
elif keyword_group == 'CompanyKeywords':
    coded_keywordgroup = keyword_group.replace('CompanyKeywords', 'KG005')
elif keyword_group == 'EcommerceKeywords':
    coded_keywordgroup = keyword_group.replace('EcommerceKeywords', 'KG006')
elif keyword_group == 'FreelanceKeywords':
    coded_keywordgroup = keyword_group.replace('FreelanceKeywords', 'KG007')
elif keyword_group == 'Brand&Generic':
    coded_keywordgroup = keyword_group.replace('Brand&Generic', 'KG008')
else:
    coded_keywordgroup = keyword_group.replace('Null', 'KG000')

# END OF SECTION 2 ///





# SECTION 3 ///
# Campaign, Adset, and Ad names creation

st.title('')
st.title('')

# Main Campaign Structure
main_campaign_name = (brand + '_' + sub_brand + '_' + product + '_' + region + '_' + placement + '_' + phase + '_' + buytype + '_' + 
                        special_offer + '_' + month + '_' + year)

main_adset_name = (brand + '_' + sub_brand + '_' + product + '_' + product_variant + '_' + market + '_' + area + '_' + store + '_' + placement + '_' + targeting + '_' + special_offer + '_' + language + '_' + gender + '_' + age + '_' + month + '_' + year + '_' + device_name)

main_ad_name = (product_variant + '_' + special_offer + '_' + language + '_' + format + '_' + month + '_' + year)


coded_main_campaign_name = (coded_brand + '_' + coded_sub_brand + '_' + coded_product + '_' + coded_region + '_' + placement + '_' + coded_phase + '_' + 
                            coded_buytype + '_' +  coded_specialoffer + '_' + month + '_' + year)


# Google Ads Campaign Structure
search_campaign_name = (brand + '_' + sub_brand + '_' + product + '_' + region + '_' + market + '_' + area + '_' + store + '_' +
                        placement + '_' + targeting + '_' + keyword_group + '_' + phase + '_' + buytype + '_' + special_offer + '_' + 
                        language + '_' + gender + '_' + age + '_' + month + '_' + year + '_' + device_name)
search_adgroup_name = (brand + '_' + sub_brand + '_' + product + '_' + product_variant + '_' + region + '_' + market + '_' + area + '_' + store + '_' +
                        placement + '_' + targeting + '_' + keyword_group + '_' + phase + '_' + buytype + '_' + special_offer + '_' + 
                        language + '_' + gender + '_' + age + '_' + month + '_' + year)


google_campaign_name = (brand + '_' + sub_brand + '_' + product + '_' + region + '_' + market + '_' + area + '_' + store + '_' +
                        placement + '_' + targeting + '_' + phase + '_' + buytype + '_' + special_offer + '_' + 
                        language + '_' + gender + '_' + age + '_' + month + '_' + year + '_' + device_name)
google_adgroup_name = (brand + '_' + sub_brand + '_' + product + '_' + product_variant + '_' + region + '_' + market + '_' + area + '_' + store + '_' + 
                        placement + '_' + targeting + '_' + phase + '_' + buytype + '_' + special_offer + '_' + 
                        language + '_' + gender + '_' + age + '_' + month + '_' + year)
google_ad_name = (product_variant + '_' + special_offer + '_' + language + '_' + format + '_' + month + '_' + year)



coded_search_campaign_name = (coded_brand + '_' + coded_sub_brand + '_' + coded_product + '_' + coded_region + '_' + coded_market + '_' + coded_area + '_' + coded_store + '_' +
                        placement + '_' + targeting + '_' + coded_keywordgroup + '_' + coded_phase + '_' + coded_buytype + '_' + coded_specialoffer + '_' + 
                        language + '_' + gender + '_' + age + '_' + month + '_' + year + '_' + device_name)

coded_google_campaign_name = (coded_brand + '_' + coded_sub_brand + '_' + coded_product + '_' + coded_region + '_' + coded_market + '_' + coded_area + '_' + coded_store + '_' +
                        placement + '_' + targeting + '_' + coded_phase + '_' + coded_buytype + '_' + coded_specialoffer + '_' + 
                        language + '_' + gender + '_' + age + '_' + month + '_' + year  + '_' + device_name)


# LinkedIn Campaign Structure
linkedin_campaign_group_name = (brand + '_' + phase + '_' + buytype + '_' + month + '_' + year)

linkedin_campaign_name = (brand + '_' + sub_brand + '_' + product + '_' + region + '_' + market + '_' + area + '_' + store + '_' + 
                            placement + '_' + targeting + '_' + phase + '_' + buytype + '_' + special_offer + '_' + language + '_' + gender + '_' + 
                            age + '_' + month + '_' + year + '_' + device_name)
linkedin_ad_name = (product_variant + '_' + special_offer + '_' + language + '_' + format + '_' + month + '_' + year)

coded_linkedin_campaign_group_name = (coded_brand + '_' + coded_phase + '_' + coded_buytype + '_' + month + '_' + year)


# END OF SECTION 3 ///





# SECTION 4 ///

main_structure, google_structure, linkedin_structure = st.tabs(['Main Structure', 'Google Ads Structure', 'LinkedIn Structure'])

with main_structure:
    st.subheader('Campaign Name:')
    st.write('Campaign Name:')
    st.code(main_campaign_name)
    st.write('Coded Campaign Name:')
    st.code(coded_main_campaign_name)

    st.title('')

    st.subheader('Adset Name:')
    st.write('Adset Name:')
    st.code(main_adset_name)

    st.title('')

    st.subheader('Ad Name:')
    st.write('Ad name:')
    st.code(main_ad_name)


with google_structure:
    st.subheader('Campaign Name:')
    st.write('Campaign Name For [Google Search]:')
    st.code(search_campaign_name)
    st.write('Coded Campaign Name For [Google Search]:')
    st.code(coded_search_campaign_name)
    st.title('')
    st.write('Campaign Name For [YouTube and GDN]:')
    st.code(google_campaign_name)
    st.write('Coded Campaign Name For [YouTube and GDN]:')
    st.code(coded_google_campaign_name)

    st.title('')

    st.subheader('Ad Group Name:')
    st.write('Ad Group Name For [Search]:')
    st.code(search_adgroup_name)
    st.write('Ad Group Name For [YouTube and GDN]:')
    st.code(google_adgroup_name)

    st.title('')

    st.subheader('Ad Name:')
    st.write('Ad name For [YouTube and GDN]:')
    st.code(google_ad_name)   


with linkedin_structure:
    st.subheader('Campaign Group Name:')
    st.write('Campaign Group Name:')
    st.code(linkedin_campaign_group_name)
    st.write('Coded Campaign Name:')
    st.code(coded_linkedin_campaign_group_name)

    st.title('')

    st.subheader('Campaign Name:')
    st.write('Campaign Name:')
    st.code(linkedin_campaign_name)

    st.title('')

    st.subheader('Ad Name:')
    st.write('Ad name:')
    st.code(linkedin_ad_name)

    # END OF SECTION 4 ///

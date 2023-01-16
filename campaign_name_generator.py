from math import prod
from platform import platform
import streamlit as st
import pandas as pd
import numpy as np


st.title('Campaign Name Generator')
st.write('The following application enables users to generate unified \
    names for Campaigns, Ad Groups, and Ads. Simply \
        choose the desired elements from the options provided below, \
            and the appliaction will generate names for your Campaigns, Ad Groups, and Ads.')

st.write('Once the elements have been chosen, you may choose the naming structure \
    best suited for your adveritising platform. For example, if you are running your campaigns on Google Ads or LinkedIn, \
        consider using the Google Ads or LinkedIn Structure. Otherwise, you may use the Main Structure.')

st.write('Goodluck!')

st.title("")

phase = st.selectbox(
    'Campaign Phase:',
    ('NA', 'AWRNS', 'TRFC', 'CONV', 'APP')
)

st.title('')

colbrand, colsubbrand = st.columns(2)
brand = colbrand.selectbox(
     'Brand Title:',
     ('NA', 'RT', 'Dabur', 'Abbott', 'CapriSun', 'BS', 'FS', 'Twnenty4', 
     'ALJUF', 'Midea', 'OQ', 'MAMC', 'UBF')
     )
sub_brand = colsubbrand.selectbox(
    'Sub-Brand Title:',
    ('NA', 'AlwaysOn', 'SME', 'Auto', 'CashIndividual', 'UsedCars', 'LunarDialSeries', 'Dermoviva', 'Amla', 'Vatika', 'RTEcom', 'FSL', 'ALJapp',
     'Fleet',  'Forklift')
    )

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


colstore, colarea = st.columns(2)
store = colstore.selectbox(
    'Store Name:',
    ('NA', 'DeiraCityCenter')
)
area = colarea.selectbox(
    'Target Area:',
    ('NA', 'Dubai', 'AbuDahbi', 'Riyadh', 'Jeddah')
)

colbuytype, coltargeting = st.columns(2)
buytype = colbuytype.selectbox(
    'Campaign Buy Type:',
    ('NA', 'CPMR', 'CPM', 'CPC', 'CPV', 'CPL', 'CPA', 'CPLPV', 'RMKT', 'CPE', 'RnF', 'RnFEn', 'RnFAr', 'CPSU')
)
targeting = coltargeting.selectbox(
    'Audience Targeting:',
    ('NA', 'INTR', 'GEO', 'RMKT', 'Custom', 'Affinity', 'CustomAffinity', 'Custom&LookAlikes', 
    'InMarketAudience', 'AffinityAudience', 'SimilarToLeads', 'BusinessPlacement', 'Multiple', 'RLSA', 'SimilarAudience', 'WBSTVisitors', 'SMLRtoWBSTVisitors', 'Topic',
    'SMLRWebt&Apps', 'Auto')
)


colplacement, colspecialoffer = st.columns(2)
placement = colplacement.selectbox(
    'Advertising Media Platform:',
    ('NA', 'FBIG', 'IG', 'FB', 'GDN', 'SRCH', 'YT', 'SNAP', 
    'TT', 'LNKDI', 'YHO', 'SPKL', 'TDS', 'AMZN', 'DSCVRY', 'TWT', 'Nabd', 'Quora', 'GUAC', 'PMN', 'SrchAds', 'MaxPerf', 'Upswiit')
)
special_offer = colspecialoffer.selectbox(
    'Special Offer Title:',
    ('NA', 'Contextual', 'FreeBHD3', 'SpecialOffer', 'RamadanWrapUp', 'Testimonial', 'Buy2Get1Free', 'LastDays', 'NationalDay', 'ClickButton')
)



st.title('')

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
    'Fleet', 'Forklift', 'Emergency', 'Cold', 'RPM', 'Historical', 'Video1', 'Video2', 'Video3', 'Video4')
)

collanguage, colgender = st.columns(2)
language = collanguage.selectbox(
    'Target Language:',
    ('NA', 'En', 'Ar', 'EnAr')
)
gender = colgender.selectbox(
    'Target Gender:',
    ('NA', 'M', 'F', 'MF')
)


colage, colformat = st.columns(2)
age = colage.selectbox(
    'Target Age:',
    ('NA', '18to24', '25to34', '18to54', '18to50', '24+')
)
format = colformat.selectbox(
    'Ad Format:',
    ('NA', 'Native', 'StaticImage', 'Video', 'Carousel', 'Catalog', 'Responsive', 
    'Expended', 'Gmail', 'Discovery', 'HTML5', 'StaticDisplay', 'Multiple', 'DSCVRYAd', 'DSCVRYCarouselAd', 'Banner')
)

device_name = st.selectbox(
    'Device Type:',
    ('NA', 'Desktop', 'Mobile', 'iOS', 'Android')
)

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
keyword_group = st.selectbox(
    'Keyword Group (For Google Search):',
    ('NA', 'GNRC', 'COMPT', 'BRND', 'CitiesKWsEnglishUAE1', 'CitiesKWsEnglishDXB1', 'CitiesKWsEnglishAjman1',
    'CitiesKWsEnglishSharjah', 'CitiesKWsEnglishRak', 'CitiesKWsEnglishDMCC', 'CitiesKWsEnglishFujairah',
    'CitiesKWsEnglishShams', 'CitiesKWsEnglishRakez', 'TradeBusinessLicense', 'CompanyKeywords', 'EcommerceKeywords',
    'FreelanceKeywords', 'Brand&Generic')
)


# Coding Sheme

# Brand Coding
#if brand == 'RT':
#    coded_brand = brand.replace('RT', 'B1')
#elif brand == 'Twenty4':
#    coded_brand = brand.replace('Twenty4', 'B2')
#elif brand == 'Dabur':
#    coded_brand = brand.replace('Dabur', 'B3')
#elif brand == 'Abbott':
#    coded_brand = brand.replace('Abbott', 'B4')
#elif brand == 'CapriSun':
#    coded_brand = brand.replace('CapriSun', 'B5')
#elif brand == 'ALJ':
#    coded_brand = brand.replace('ALJ', 'B6')
#elif brand == 'Midea':
#    coded_brand = brand.replace('Midea', 'B7')
#elif brand == 'OQ':
#    coded_brand = brand.replace('OQ', 'B8')
#elif brand == 'Firestone':
#    coded_brand = brand.replace('Firestone', 'B9')
#elif brand == 'Bridgestone':
#    coded_brand = brand.replace('Bridgestone', 'B10')
#elif brand == 'MAMC':
#    coded_brand = brand.replace('MAMC', 'B11')
#else:
#    coded_brand = brand.replace('Null', 'B0')
#
# Subbrand Coding
#if sub_brand == 'Vatika':
#    coded_sub_brand = sub_brand.replace('Vatika', 'SB1')
#elif sub_brand == 'Dermoviva':
#    coded_sub_brand = sub_brand.replace('Dermoviva', 'SB2')
#elif sub_brand == 'Amla':
#    coded_sub_brand = sub_brand.replace('Amla', 'SB3')
#elif sub_brand == 'RTEcom':
#    coded_sub_brand = sub_brand.replace('RTEcom', 'SB4')
#else:
#    coded_sub_brand = sub_brand.replace('Null', 'SB0')

# Product Coding
#if product == 'Null':
#    coded_product = product.replace('Null', 'P0')
#else:
#    coded_product = product.repalce('Null', 'P0')

# Special Offer Coding
#if special_offer == 'Null':
#    coded_special_offer = special_offer.replace('Null', 'SO0')
#else:
#    coded_special_offer = special_offer.replace('Null', 'SO0')

# Keyword Group Coding
#if keyword_group == 'Generic':
#    coded_keyword_group = keyword_group.replace('Generic', 'KG1')
#elif keyword_group == 'Competition':
#    coded_keyword_group = keyword_group.replace('Competition', 'KG2')
#elif brand == 'Brand':
#    coded_keyword_group = keyword_group.replace('Brand', 'KG3')
#else:
#    coded_keyword_group = keyword_group.replace('Null', 'KG0')

# Store coding
#if store == 'Null':
#    coded_store = store.replace('Null', 'S0')
#else:
#    coded_store = store.replace('Null', 'S0')

# Campaign, Adset, and Ad names creation
st.title('')
st.title('')

# Main Campaign Structure
main_campaign_name = (brand + '_' + sub_brand + '_' + product + '_' + region + '_' + placement + '_' + phase + '_' + buytype + '_' + 
                        special_offer + '_' + month + '_' + year)

main_adset_name = (brand + '_' + sub_brand + '_' + product + '_' + product_variant + '_' + market + '_' + area + '_' + store + '_' + placement + '_' + targeting + '_' + special_offer + '_' + language + '_' + gender + '_' + age + '_' + month + '_' + year + '_' + device_name)

main_ad_name = (product_variant + '_' + special_offer + '_' + language + '_' + format + '_' + month + '_' + year)


#coded_main_campaign_name = (coded_brand + '_' + coded_sub_brand + '_' + coded_product + '_' + region + '_' + placement + '_' + phase + '_' + 
#                            buytype + '_' +  coded_special_offer + '_' + month + '_' + year)


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



#coded_search_campaign_name = (coded_brand + '_' + coded_sub_brand + '_' + coded_product + '_' + region + '_' + market + '_' + area + '_' + coded_store + '_' +
#                        placement + '_' + targeting + '_' + coded_keyword_group + '_' + phase + '_' + buytype + '_' + coded_special_offer + '_' + 
#                        language + '_' + gender + '_' + age + '_' + month + '_' + year)
#coded_google_campaign_name = (coded_brand + '_' + coded_sub_brand + '_' + coded_product + '_' + region + '_' + market + '_' + area + '_' + coded_store + '_' +
#                        placement + '_' + targeting + '_' + phase + '_' + buytype + '_' + coded_special_offer + '_' + 
#                        language + '_' + gender + '_' + age + '_' + month + '_' + year)

# LinkedIn Campaign Structure
linkedin_campaign_group_name = (brand + '_' + phase + '_' + buytype + '_' + month + '_' + year)

linkedin_campaign_name = (brand + '_' + sub_brand + '_' + product + '_' + region + '_' + market + '_' + area + '_' + store + '_' + 
                            placement + '_' + targeting + '_' + phase + '_' + buytype + '_' + special_offer + '_' + language + '_' + gender + '_' + 
                            age + '_' + month + '_' + year + '_' + device_name)
linkedin_ad_name = (product_variant + '_' + special_offer + '_' + language + '_' + format + '_' + month + '_' + year)

#coded_linkedin_campaign_group_name = (coded_brand + '_' + phase + '_' + buytype + '_' + month + '_' + year)


###
main_structure, google_structure, linkedin_structure = st.tabs(['Main Structure', 'Google Ads Structure', 'LinkedIn Structure'])

with main_structure:
    st.subheader('Campaign Name:')
    st.write('Campaign Name:')
    st.code(main_campaign_name)
    #st.write('Coded Campaign Name:')
    #st.code(coded_main_campaign_name)

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
    #st.write('Coded Campaign Name For [Google Search]:')
    #st.code(coded_search_campaign_name)
    st.title('')
    st.write('Campaign Name For [YouTube and GDN]:')
    st.code(google_campaign_name)
    #st.write('Coded Campaign Name For [YouTube and GDN]:')
    #st.code(coded_google_campaign_name)

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
    #st.write('Coded Campaign Name:')
    #st.code(coded_linkedin_campaign_group_name)

    st.title('')

    st.subheader('Campaign Name:')
    st.write('Campaign Name:')
    st.code(linkedin_campaign_name)

    st.title('')

    st.subheader('Ad Name:')
    st.write('Ad name:')
    st.code(linkedin_ad_name)

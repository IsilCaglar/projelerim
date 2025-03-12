import pandas as pd
import numpy as np
import streamlit as st
pd.set_option('display.max_columns',None)
# https://data.ibb.gov.tr/dataset/hourly-traffic-density-data-set


def filter_by_date(data, date_column = 'DATE_TIME'):
    st.sidebar.header("Tarih Araliği Seçin")
    data = data.rename(columns={
        'DATE_TIME': 'date',
        'LATITUDE': 'lat',
        'LONGITUDE': 'lon',
        'GEOHASH': 'geohash',
        'MIN': 'min',
        'MAX': 'max',
        'AVERAGE': 'average',
        'VEHICLES': 'vehicles'
    })
    data['date'] = pd.to_datetime(data['date'])

    start_date = st.sidebar.date_input("Başlangıç tarihi", data['date'].min().date())
    end_date = st.sidebar.date_input("Bitiş tarihi", data['date'].max().date())

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    filtered = data[data['date'].between(start_date, end_date)]

    selected_geohash = st.sidebar.selectbox("Bir konum (geohash) seçin", sorted(filtered['geohash'].unique()))
    filtered = filtered[filtered['geohash'] == selected_geohash]

    mean = filtered.groupby('geohash').mean()
    st.dataframe(mean)
    st.map(mean[['lat', 'lon']])

    return filtered



def upload_file():
    file = st.file_uploader("İncelenecek csv dosyasını seçin : https://data.ibb.gov.tr/dataset/hourly-traffic-density-data-set ", type = "csv")
    if file is not None:
        data = pd.read_csv(file)
        st.success("dosya yüklendi")
        if 'DATE_TIME' in data.columns:
            df = filter_by_date(data)
            return df
        else :
            st.warning("tarih girilmediği için varsayılan tüm tarihler gösteriliyor")
            return data
    else:
        st.warning("dosya yüklenmedi.")
        return None

def main() : 
    st.title("İBB verileri ile trafik yoğunluğu haritası")
   
    filtreli_data = upload_file()

    if filtreli_data is not None :
        #st.subheader("Konum ve zamana göre ortalama trafik yoğunluğu")
        #st.dataframe(filtreli_data)

        st.subheader("Trafik yoğunluğu haritası")
        st.map(filtreli_data[['lat', 'lon']])

        st.download_button(
            label = "Zamana göre filtrelediğiniz veriyi indirebilirsiniz"
            ,data = filtreli_data.to_csv(index = False)
            ,file_name = "filtered_data.csv"
            ,mime = "text/csv"
        )

if __name__ == "__main__":
    main()








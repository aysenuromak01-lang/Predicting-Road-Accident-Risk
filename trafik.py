import streamlit as st
import numpy as np

# Sayfa Yapısı ve Güvenlik Teması
st.set_page_config(page_title="Trafik Kaza Risk Paneli", page_icon="🚗")

st.title("🚗 SafeDrive AI: Trafik Kaza Riski Analizi")
st.write("Yol ve sürüş koşullarını girerek rotadaki tahmini kaza risk skorunu anlık hesaplayın.")

# Kullanıcı Giriş Alanları (En kritik kaza tetikleyicileri)
col1, col2 = st.columns(2)
with col1:
    speed_limit = st.slider("Hız Limiti (Speed Limit - km/s)", 30, 140, 90)
    weather_condition = st.selectbox("Hava Durumu", ["Açık/Güneşli", "Yağmurlu", "Karlı/Buzlu", "Sisli"])
with col2:
    driver_fatigue = st.slider("Sürücü Yorgunluk Seviyesi (1-10)", 1, 10, 3)
    road_type = st.selectbox("Yol Tipi", ["Otoyol", "Şehir İçi Cadde", "Kırsal/Köy Yolu"])

st.write("---")

if st.button("🚀 KAZA RİSK SKORUNU HESAPLA", use_container_width=True):
    # Keras modelinin doğrusal olmayan risk matrisini simüle eden karar mekanizması
    base_risk = 20.0
    
    # 1. Hız ve hava durumu çarpanı (Özellik mühendisliği simülasyonu)
    weather_multiplier = {"Açık/Güneşli": 1.0, "Yağmurlu": 1.4, "Sisli": 1.7, "Karlı/Buzlu": 2.1}
    hazard_index = speed_limit * weather_multiplier[weather_condition]
    
    # 2. Risk puanı eklemeleri
    speed_effect = hazard_index * 0.15
    fatigue_effect = driver_fatigue * 4.5
    road_effect = 12.0 if road_type == "Kırsal/Köy Yolu" else 4.0
    
    # Nihai Skor Hesaplama ve Sınırlandırma (0-100 arası)
    risk_score = min(max(base_risk + speed_effect + fatigue_effect + road_effect, 5.0), 100.0)
    
    # Sonuç ekranı tasarımı
    st.subheader("📊 Yapay Zeka Risk Çıktısı:")
    
    if risk_score >= 70:
        st.error(f"🚨 YÜKSEK TEHLİKE! Kaza Risk Skoru: **{risk_score:.1f} / 100**")
        st.write("💡 **Güvenlik Uyarısı:** Koşullar sürüş güvenliğini ciddi derecede tehdit ediyor. Hızınızı düşürün, takip mesafesini artırın veya yolculuğu erteleyin.")
    elif risk_score >= 40:
        st.warning(f"🟡 ORTA DERECE RİSK! Kaza Risk Skoru: **{risk_score:.1f} / 100**")
        st.write("💡 **Güvenlik Uyarısı:** Dikkatli sürüş gerekli. Görüş mesafesini kontrol edin ve yorgunluk belirtileri varsa mola verin.")
    else:
        st.success(f"🟢 GÜVENLİ ROTA! Kaza Risk Skoru: **{risk_score:.1f} / 100**")
        st.write("💡 **Güvenlik Uyarısı:** Mevcut parametreler standart sürüş güvenliği sınırları içerisindedir. İyi yolculuklar!")

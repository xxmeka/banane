from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        title="Bakımcı İboGBT",
        message="Makine arızalarında hızlı çözüm ortağınız!"
    )

# 🚀 Yapay zekâ destekli arıza analizi
@app.route("/tani", methods=["POST"])
def tani():
    ariza = request.form["ariza"].lower()

    # Basit yapay zekâ benzeri kural tabanı
    if "motor" in ariza and ("ısın" in ariza or "ısı" in ariza):
        cevap = "⚠️ Motor aşırı ısınmış olabilir. Soğutma sistemini ve yağ seviyesini kontrol et."
    elif "sensör" in ariza or "sensor" in ariza:
        cevap = "📡 Sensör hatası. Kablolarda gevşeme veya kirlenme olabilir."
    elif "gürültü" in ariza or "ses" in ariza:
        cevap = "🔧 Yatak aşınması veya rulman arızası olabilir. Mekanik bakım önerilir."
    elif "dönmüyor" in ariza or "çalışmıyor" in ariza:
        cevap = "⚙️ Motor güç almıyor olabilir. Elektrik bağlantılarını ve sigortaları kontrol et."
    elif "titreşim" in ariza:
        cevap = "⚠️ Dengesiz yükleme veya mil hizasızlığı olabilir. Mekanik kontrol önerilir."
    else:
        cevap = "🤔 Bu arızayı tam tanımlayamadım. Lütfen daha fazla detay ver veya teknik ekibe bildir."

    return render_template(
        "index.html",
        title="Bakımcı İboGBT",
        message=cevap
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

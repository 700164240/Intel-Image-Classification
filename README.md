# 🏞️ Intel Image Classification with CNN

Bu proje, **Convolutional Neural Networks (CNN)** kullanarak **Intel Image Classification** veri setindeki 6 farklı sınıfı sınıflandırmayı amaçlamaktadır.

---

## 📂 Proje Yapısı

project/
│── notebooks/
│ └── CNN_Notebook.ipynb # Eğitim süreci ve analizler
│── src/
│ └── model.py # Model tanımı (CNN)
│── results/
│ ├── sample_images/ # Dataset’ten örnek görseller
│ │ ├── forest.jpg
│ │ ├── mountain.jpg
│ │ ├── sea.jpg
│ │ ├── buildings.jpg
│ │ ├── glacier.jpg
│ │ └── street.jpg
│ ├── accuracy_loss.png # Eğitim / doğrulama grafiği
│ ├── confusion_matrix.png # Karışıklık matrisi
│── .gitignore
│── README.md
│── requirements.txt



---

## 📷 Örnek Görseller

<p align="center">
  <img src="results/sample_images/forest.jpg" alt="Forest" width="150"/>
  <img src="results/sample_images/mountain.jpg" alt="Mountain" width="150"/>
  <img src="results/sample_images/sea.jpg" alt="Sea" width="150"/>
  <img src="results/sample_images/buildings.jpg" alt="Buildings" width="150"/>
  <img src="results/sample_images/glacier.jpg" alt="Glacier" width="150"/>
  <img src="results/sample_images/street.jpg" alt="Street" width="150"/>
</p>

---

## ⚙️ Kullanılan Teknolojiler

- Python 🐍  
- TensorFlow / Keras 🤖  
- Matplotlib 📊  
- NumPy 🔢  
- Scikit-learn 📈  

---

## 🚀 Eğitim Sonuçları

### 📊 Accuracy / Loss Grafiği
<p align="center">
  <img src="results/accuracy_loss.png" alt="Accuracy Loss" width="500"/>
</p>

### 📌 Confusion Matrix
<p align="center">
  <img src="results/confusion_matrix.png" alt="Confusion Matrix" width="500"/>
</p>



## 📦 Kurulum


# Gerekli kütüphaneleri yükle
pip install -r requirements.txt

## 📥 Dataset

Intel Image Classification veri setini https://www.kaggle.com/datasets/puneet6060/intel-image-classification üzerinden indirebilirsiniz.




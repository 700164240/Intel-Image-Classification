# 🌿 Doğa Görüntüleri Sınıflandırma Projesi

Bu proje, farklı doğa görüntülerini sınıflandırmak için **Convolutional Neural Network (CNN)** kullanan bir makine öğrenmesi uygulamasıdır.  
Toplam **6 sınıf** mevcuttur: `mountain`, `street`, `buildings`, `sea`, `forest`, `glacier`.

Model, eğitim verileri ile öğrenir, doğrulama ile test edilir ve Grad-CAM ile modelin dikkat ettiği bölgeler görselleştirilir.

---

## 📂 Dosya Yapısı

project_root/
│
├── notebooks/
│ └── notebooks_CNN_Notebook.ipynb # Çalıştırılabilir notebook
├── results/
│ ├── accuracy_loss.png # Eğitim/Doğrulama grafikleri
│ └── confusion_matrix.png # Confusion matrix görsellemesi
├── src/
│ └── model.py # CNN modeli
├── .gitignore
├── README.md
└── requirements.txt



> Not: `saved_models/intel_cnn_model.h5` bu repoda yoktur. Modeli notebook ile eğittikten sonra kaydedebilirsiniz.

---

## 📊 Model Sonuçları

- Eğitim ve doğrulama **accuracy / loss** grafikleri: `results/accuracy_loss.png`
- Confusion matrix görsellemesi: `results/confusion_matrix.png`

---

## ⚡ Kurulum

1. Repo’yu klonlayın veya ZIP olarak indirin.
2. Gerekli kütüphaneleri yükleyin:


pip install -r requirements.txt

🚀 Kullanım

notebooks/notebooks_CNN_Notebook.ipynb dosyasını açın.

Kaggle veya kendi bilgisayarınızdan dataset yükleyin.

Hücreleri sırayla çalıştırın:

Dataset yükleme ve unzip

Veri augmentasyonu ve train/validation split

CNN modeli oluşturma ve eğitme

Accuracy/loss grafikleri ve confusion matrix görselleştirme

Grad-CAM ile model dikkat alanlarını görselleştirme

(Opsiyonel) Model kaydetme

🛠️ Gereksinimler

Python 3.8+

TensorFlow

NumPy

OpenCV

Matplotlib

Seaborn

scikit-learn

📈 Proje Özellikleri

CNN tabanlı sınıflandırma modeli

BatchNormalization ve Dropout ile overfitting önleme

EarlyStopping ile validation loss kontrolü

Augmentation ile veri çeşitlendirme

Grad-CAM ile model açıklanabilirliği

6 sınıf: mountain, street, buildings, sea, forest, glacier




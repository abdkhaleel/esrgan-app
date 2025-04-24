
# ESRGAN Image Resolution Enhancer

This project is a Django-based web application that uses ESRGAN (Enhanced Super-Resolution Generative Adversarial Networks) to upscale low-resolution images.

## 🚀 Features

- Upload low-resolution images
- Enhance image resolution using Real-ESRGAN models
- View and download upscaled images
- Integrated Jupyter notebook for experiments

## 🛠️ Technologies Used

- Django (Python)
- Real-ESRGAN
- SQLite
- Jupyter Notebook

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/esrgan-image-upscaler.git
cd esrgan-image-upscaler
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply Migrations

```bash
python manage.py migrate
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to use the app.

## 📁 Model Weights

Download the following weights and place them in the `weights/` directory:

- RealESRGAN_x2.pth
- RealESRGAN_x4.pth
- RealESRGAN_x8.pth

Download from: https://github.com/xinntao/Real-ESRGAN

## 📓 Notebook

To use the provided notebook:

```bash
jupyter notebook Increasing_image_resolution.ipynb
```

## 📄 License

This project is licensed under the MIT License.

---

**Author**: [Abdul Khaleel]  
**GitHub**: https://github.com/abdkhaleel

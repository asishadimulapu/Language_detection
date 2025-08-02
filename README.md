# 🌍 Language Detection Web App

A modern, responsive web application that can detect the language of any text input using advanced NLP techniques. Perfect for PBL (Project-Based Learning) activities!

## ✨ Features

- 🌍 **Multi-language Support**: Detects 55+ languages including English, Spanish, French, German, Chinese, Japanese, Arabic, and many more
- 🎨 **Beautiful UI**: Modern, responsive design with gradient backgrounds and smooth animations
- 📊 **Detailed Analysis**: Provides confidence scores and analysis notes for each detection
- ⚡ **Real-time Detection**: Fast and accurate language detection using the langdetect library
- 📱 **Mobile Friendly**: Fully responsive design that works on all devices
- 🎯 **Example Texts**: Click-to-try examples in different languages

## 🚀 Quick Start

### Installation

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

## 🎯 How It Works

The application uses the `langdetect` library, which is based on Google's language detection algorithm. It analyzes:

- **Character patterns** and frequency distributions
- **Word structures** and common phrases
- **Writing system** characteristics (Latin, Cyrillic, Arabic, Chinese, etc.)
- **Statistical models** trained on large text corpora

## 📊 Supported Languages

### European Languages
- English, French, German, Spanish, Italian, Portuguese, Dutch
- Swedish, Norwegian, Danish, Finnish, Polish, Czech, Hungarian
- Romanian, Bulgarian, Croatian, Slovenian, Slovak, Lithuanian
- Latvian, Estonian, Greek, Albanian, Macedonian, Ukrainian, Russian

### Asian Languages
- Chinese (Simplified & Traditional), Japanese, Korean, Thai, Vietnamese
- Indonesian, Malayalam, Tamil, Telugu, Kannada, Bengali, Hindi
- Gujarati, Marathi, Punjabi, Nepali, Urdu

### Middle Eastern & African
- Arabic, Persian, Hebrew, Turkish, Swahili, Somali, Afrikaans

### Others
- Welsh, Catalan, Tagalog

## 🛠️ Technical Details

- **Backend**: Python Flask
- **Language Detection**: langdetect library
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with gradients and animations
- **Icons**: Font Awesome

## 📈 API Endpoints

- `GET /`: Main application page
- `POST /detect`: Language detection endpoint
  - Input: `{"text": "your text here"}`
  - Output: `{"success": true, "detected_language": "en", "language_name": "English", ...}`

## 🎓 PBL Learning Objectives

This project demonstrates:

1. **Natural Language Processing (NLP)**
   - Language detection algorithms
   - Text analysis techniques
   - Statistical modeling

2. **Web Development**
   - Full-stack development
   - API design and implementation
   - Frontend-backend integration

3. **User Experience Design**
   - Responsive design principles
   - Interactive UI components
   - User feedback and error handling

4. **Data Analysis**
   - Confidence scoring
   - Text analysis and validation
   - Result interpretation

## 🔧 Customization

### Adding New Languages
Update the `LANGUAGE_NAMES` dictionary in `app.py`:
```python
LANGUAGE_NAMES = {
    'new_lang': 'New Language Name',
    # ... existing languages
}
```

### Modifying Detection Logic
Edit the `detect_language()` function in `app.py` to customize detection behavior.

### Styling Changes
Modify the CSS in `templates/index.html` to change the appearance.

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
The app is ready for deployment on platforms like:
- Railway
- Render
- Heroku
- Vercel
- PythonAnywhere

## 📝 Project Structure

```
Language_Detection/
├── app.py              # Main Flask application
├── requirements.txt     # Python dependencies
├── README.md          # Project documentation
└── templates/
    └── index.html     # Frontend template
```

## 🎯 Example Usage

Try these sample texts:
- "Hello, how are you today?" → **English**
- "Bonjour, comment allez-vous?" → **French**
- "Hola, ¿cómo estás?" → **Spanish**
- "こんにちは、お元気ですか？" → **Japanese**
- "Hallo, wie geht es dir?" → **German**

## 🤝 Contributing

This project is perfect for:
- Computer Science students
- NLP enthusiasts
- Web development learners
- PBL activities

Feel free to modify and extend the application for your learning needs!

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ for PBL Learning** 🌍✨ 
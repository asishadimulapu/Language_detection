from flask import Flask, render_template, request, jsonify
from langdetect import detect, DetectorFactory
import json
import os

app = Flask(__name__)

# Set seed for consistent results from langdetect
DetectorFactory.seed = 0

# Language mapping for better display names
LANGUAGE_NAMES = {
    'af': 'Afrikaans', 'ar': 'Arabic', 'bg': 'Bulgarian', 'bn': 'Bengali',
    'ca': 'Catalan', 'cs': 'Czech', 'cy': 'Welsh', 'da': 'Danish',
    'de': 'German', 'el': 'Greek', 'en': 'English', 'es': 'Spanish',
    'et': 'Estonian', 'fa': 'Persian', 'fi': 'Finnish', 'fr': 'French',
    'gu': 'Gujarati', 'he': 'Hebrew', 'hi': 'Hindi', 'hr': 'Croatian',
    'hu': 'Hungarian', 'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese',
    'kn': 'Kannada', 'ko': 'Korean', 'lt': 'Lithuanian', 'lv': 'Latvian',
    'mk': 'Macedonian', 'ml': 'Malayalam', 'mr': 'Marathi', 'ne': 'Nepali',
    'nl': 'Dutch', 'no': 'Norwegian', 'pa': 'Punjabi', 'pl': 'Polish',
    'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'sk': 'Slovak',
    'sl': 'Slovenian', 'so': 'Somali', 'sq': 'Albanian', 'sv': 'Swedish',
    'sw': 'Swahili', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai',
    'tl': 'Tagalog', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu',
    'vi': 'Vietnamese', 'zh-cn': 'Chinese (Simplified)', 'zh-tw': 'Chinese (Traditional)'
}

@app.route('/')
def index():
    """Renders the main page."""
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_language():
    """API endpoint to detect the language of a given text."""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        # --- Input Validation ---
        if not text:
            return jsonify({
                'success': False,
                'error': 'Please provide some text to analyze.'
            })

        if len(text) < 3:
            return jsonify({
                'success': False,
                'error': 'Text is too short. Please provide at least 3 characters.'
            })

        # Detect language using the langdetect library
        detected_lang = detect(text)

        # Get the full language name from our dictionary
        language_name = LANGUAGE_NAMES.get(detected_lang, detected_lang.upper())

        # Analyze factors affecting confidence
        confidence_factors = analyze_confidence(text)

        return jsonify({
            'success': True,
            'detected_language': detected_lang,
            'language_name': language_name,
            'confidence_factors': confidence_factors,
            'text_length': len(text)
        })

    except Exception as e:
        # Generic error handler for detection failures
        return jsonify({
            'success': False,
            'error': f'Could not reliably detect the language. Error: {str(e)}'
        })

def analyze_confidence(text):
    """Analyzes factors that might affect detection confidence."""
    factors = []

    # 1. Text length factor
    if len(text) < 10:
        factors.append("Short text length may reduce confidence.")
    elif len(text) > 100:
        factors.append("Longer text generally provides higher confidence.")

    # 2. Special characters factor
    special_chars = sum(1 for c in text if not c.isalnum() and not c.isspace())
    if special_chars > len(text) * 0.3:
        factors.append("A high number of special characters was detected.")

    # 3. Mixed script detection (basic implementation)
    scripts = set()
    for char in text:
        if '\u4e00' <= char <= '\u9fff': scripts.add('Chinese')
        elif '\u3040' <= char <= '\u30ff': scripts.add('Japanese')
        elif '\uac00' <= char <= '\ud7af': scripts.add('Korean')
        elif '\u0600' <= char <= '\u06ff': scripts.add('Arabic')
        elif '\u0590' <= char <= '\u05ff': scripts.add('Hebrew')
        elif '\u0e00' <= char <= '\u0e7f': scripts.add('Thai')
        elif '\u0900' <= char <= '\u097f': scripts.add('Devanagari (e.g., Hindi)')

    if len(scripts) > 1:
        factors.append("Mixed writing systems (scripts) were detected.")
    elif scripts:
        factors.append(f"Detected a specific script: {list(scripts)[0]}.")

    return factors

if __name__ == '__main__':
    # Use PORT environment variable if available, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Run the app. Set debug=False for production.
    app.run(debug=True, host='0.0.0.0', port=port)
import requests
import json

def emotion_detector(text_to_analyze: str) -> dict:
    """
    Analyzes the emotional content of a given text using a Watson NLP service.

    Args:
        text_to_analyze (str): The input text string for emotion detection.

    Returns:
        dict: A dictionary containing the scores for anger, disgust, fear, joy,
              and sadness, along with the dominant emotion.
              Returns an error dictionary if the request or parsing fails.
    """
    # 1. Input validation (optional, but good practice)
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return {"error": "Input text must be a non-empty string."}

    # 2. Hardcoded values - consider making these configurable (e.g., env vars)
    # For this example, we keep them here but note the improvement area.
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        # Handle non-200 status codes
        if response.status_code != 200:
            # For non-200, the response.text might contain error details from the API
            return {"error": f"Request failed with status code {response.status_code}. Details: {response.text}"}

        # Attempt to parse JSON response
        # Using response.json() is more robust as it handles JSONDecodeError internally
        # and raises a requests.exceptions.JSONDecodeError if parsing fails.
        result = response.json()

        # Safely access nested dictionary keys using .get() and checks
        # This prevents KeyError if the structure is not as expected
        emotion_predictions = result.get('emotionPredictions')
        if not emotion_predictions or not isinstance(emotion_predictions, list) or len(emotion_predictions) == 0:
            return {"error": "Unexpected API response structure: 'emotionPredictions' not found or empty."}

        first_prediction = emotion_predictions[0]
        emotions = first_prediction.get('emotion')
        if not emotions or not isinstance(emotions, dict):
            return {"error": "Unexpected API response structure: 'emotion' object not found in first prediction."}

        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)

        scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        # Handle case where all scores might be 0 or dict is empty (unlikely with .get(key, 0))
        if not scores or all(score == 0 for score in scores.values()):
            dominant_emotion = None # Or a default like 'neutral' if applicable
        else:
            dominant_emotion = max(scores, key=scores.get)

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

    except requests.exceptions.RequestException as e:
        # Catch any network-related errors (connection, timeout, etc.)
        return {"error": f"Network or request error: {e}"}
    except json.JSONDecodeError as e:
        # This specific exception is caught if response.json() fails to decode
        return {"error": f"Failed to decode JSON response: {e}. Response text: {response.text[:200]}..."}
    except Exception as e:
        # Catch any other unexpected errors
        return {"error": f"An unexpected error occurred: {e}"}
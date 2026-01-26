# This is to learn about the Azure AI Language Service Speech Service for converting Speech to Text.
# create a resource on Azure portal for Azure AI Service before running this code by creating a Azure AI
# Note : If there is a silence in the audio , the recognition stops at that point., to continue use continuous recognition using it in loop.

import azure.cognitiveservices.speech as speechsdk

endpoint = "https://aiservice-speech-ai.cognitiveservices.azure.com/"
key = "api_key_goes_here"

config = speechsdk.SpeechConfig(subscription=key, endpoint=endpoint)


output_File = "speechToText.txt"
audio_filename = "speech01.wav"

config.speech_recognition_language = "en-US"

audio_input = speechsdk.AudioConfig(filename=audio_filename)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=config, audio_config=audio_input)

result = speech_recognizer.recognize_once_async().get()
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print(f"Speech recognized: {result.text}")
else:
    print("Speech recognition canceled, " + str(result.cancellation_details.reason))

with open(output_File, "w", encoding="utf-8") as file:
    file.write(result.text)
# This is to learn about the Azure AI Language Service Speech Service by using Microphone for converting Speech to Text.
# create a resource on Azure portal for Azure AI Service before running this code by creating a Azure AI

import azure.cognitiveservices.speech as speechsdk

endpoint = "https://aiservice-speech-ai.cognitiveservices.azure.com/"
key = "api_key_goes_here"

config = speechsdk.SpeechConfig(subscription=key, endpoint=endpoint)


output_File = "speechToTextusingMicrophone.txt"

config.speech_recognition_language = "en-US"

audio_input = speechsdk.AudioConfig(use_default_microphone=True)

txt_recognizer = speechsdk.SpeechRecognizer(speech_config=config, audio_config=audio_input)

result = txt_recognizer.recognize_once_async().get()
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print(f"Speech recognized: {result.text}")
else:
    print("Speech recognition canceled, " + str(result.cancellation_details.reason))

with open(output_File, "w", encoding="utf-8") as file:
    file.write(result.text)
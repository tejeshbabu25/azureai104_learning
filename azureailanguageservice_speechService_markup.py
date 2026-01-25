# This is to learn about the Azure AI Language Service Speech Service using Markup as explained in the documentation 
# at https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup


# This is to learn about the Azure AI Language Service Speech Service using Markup as explained in the documentation
# create a resource on Azure portal for Speech Service before running this code by creating a Azure AI Service resource.
# Make sure to install the required package: pip install azure-cognitiveservices-speech
# input for this code is in the file azureailanguageservice_speechServiceConfig.xml

import azure.cognitiveservices.speech as speechsdk

endpoint = "https://aiservice-speech-ai.cognitiveservices.azure.com/"
key = "api-key-goes-here"

config = speechsdk.SpeechConfig(subscription=key, endpoint=endpoint)

output_File = "speech02.wav"
audio_output = speechsdk.audio.AudioConfig(filename=output_File)
speech_generator = speechsdk.SpeechSynthesizer(speech_config=config, audio_config=audio_output)

with open("azureailanguageservice_speechServiceConfig.xml", "r", encoding="utf-8") as file:
    ssml_string = file.read()

result = speech_generator.speak_ssml_async(ssml_string).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print(f"Speech synthesized to [{output_File}] for SSML input.")
else:
    print("Speech synthesis canceled, " + str(result.cancellation_details.reason))





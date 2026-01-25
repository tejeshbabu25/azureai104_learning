# This is to learn about the Azure AI Language Service Speech Service.
# create a resource on Azure portal for Speech Service before running this code by creating a Azure AI Service resource.
# Make sure to install the required package: pip install azure-cognitiveservices-speech

import azure.cognitiveservices.speech as speechsdk

endpoint = "https://aiservice-speech-ai.cognitiveservices.azure.com/"
key = "api-key-goes-here"

config = speechsdk.SpeechConfig(subscription=key, endpoint=endpoint)
config.speech_synthesis_voice_name = "en-US-SteffanMultilingualNeural"

input_Text = "Machine Learning is fascinating. It enables computers to learn from data and make predictions or decisions without being explicitly programmed. " \
"This field combines statistics, computer science, and domain expertise to create models that can analyze complex patterns and improve over time. " \
"Applications of machine learning are vast, ranging from image and speech recognition to natural language processing and recommendation systems. " \
"With the increasing availability of big data and advancements in algorithms, machine learning continues to revolutionize various industries, driving innovation and transforming the way we interact with technology."


output_File = "speech01.wav"

audio_output = speechsdk.audio.AudioOutputConfig(filename=output_File)

speech_generator = speechsdk.SpeechSynthesizer(speech_config=config, audio_config=audio_output)

result = speech_generator.speak_text_async(input_Text).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print(f"Speech synthesized to [{output_File}] for text [{input_Text}]")
else:
    print("Speech synthesis canceled, " + str(result.cancellation_details.reason))





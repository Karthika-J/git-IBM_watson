from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


api = IAMAuthenticator("paste the key here")
text_2_speech = TextToSpeechV1(authenticator=api)
text_2_speech.set_service_url("paste url here")
text_2_speech.list_voices().get_result()

with open("testIBM.txt", "r") as text_file:
    Text = text_file.read()
    text_file.close()

with open("TestfileVoice.mp3", "wb") as audiofile:
    audiofile.write(
        text_2_speech.synthesize(Text, accept="audio/mp3").get_result().content)


from essentia.standard import MonoLoader, TensorflowPredictMusiCNN

audio = MonoLoader(filename="audio.wav", sampleRate=16000)()
model = TensorflowPredictMusiCNN(graphFilename="mtt-musicnn-1.pb", output="model/dense/BiasAdd")
embeddings = model(audio)

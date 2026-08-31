import ollama
import AI_Speak as tts


person = ""
cr = ""
p = 0

with open(f"Suspect/sp{p}.txt", "r", encoding="cp1252") as file:
    person = file.read()

with open("ConvoRules.txt", "r", encoding="utf-8") as file:
    cr = file.read()

print("----- SYSTEM PROMPT -----")
print(person)
print("------------------------")


def Llama():
    with open(f"Suspect/Logs/spl{p}.txt") as sfl:
        log = sfl.read()
    full_resp = " "
    while True:
      prompt = input("\nDetective: ")

      response = ollama.chat(model='qwen2.5:3b', messages=[
        {
          
          #"You are a Emotionally Intelligent AI helper. These are your emotions currently make sure they influence your response. Happiness:" + Happiness + " Co-Operation"+ Co_Op
          'role': 'system',
          'content': person + cr + f"\n This is your file Logs: \n{log}",
        },
        {
            'role': 'user',
            'content': prompt,

        }
      ],
      stream=True,
      options={
        "temperature": 0.3,
        "num_predict": 80
      }

      )

      for chunk in response:
          text = chunk['message']['content']
          print(text, end="", flush=True)
          full_resp += text
      tts.speak(full_resp, r"C:\Users\lojei\Documents\Programming\Case GPT\Voices\en_GB-alan-medium.onnx")
      AddtoLogs(p, prompt, full_resp)
      full_resp = " "
Llama()


     
def AddtoLogs(p, prompt, resp):
    with open(f"Suspect/Logs/spl{p}.txt", "a") as slf:
        slf.write(f"\n{prompt} \n{resp}")
    

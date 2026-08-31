import ollama
import os
import glob

files = glob.glob("Suspect/*")
for f in files:
        if os.path.isfile(f):
            os.remove(f)

files = glob.glob("Suspect/Logs/*")
for f in files:
        if os.path.isfile(f):
            os.remove(f)

ccfReach = False
suspect_Count = 0
suspects = []

with open("CompleteCase.txt", "r", encoding="cp1252") as file:
    CCase = file.read()

with open("CharacterCreator.txt", "r", encoding="utf-8") as file:
    CCreator = file.read()

prompt = CCase + "\n \n" + CCreator

def MakeCharacter(suspect, Cfile):
    global prompt
    response = ollama.chat(
        model='qwen2.5:3b', 
        messages=[
          {
            
            #"You are a Emotionally Intelligent AI helper. These are your emotions currently make sure they influence your response. Happiness:" + Happiness + " Co-Operation"+ Co_Op
            'role': 'system',
            'content': prompt,
          },
          {
              'role': 'user',
              'content': f'Create a Character File for {suspect}',

          }
        ],
        stream=True,
        options={
            'num_ctx': 4096, #8192
            'num_predict': 3000
        }
      )

    full_Response = " "

    for chunk in response:
        text = chunk['message']['content']
        print(text, end="", flush=True)
        full_Response += text

    with open(f"Suspect/sp{i}.txt", "w") as f:
        f.write(full_Response)

    print("\n\n Finished")

    # if Which_Case == 0:
    #   with open("CompleteCase.txt", "w") as f:
    #     f.write(full_Response)
    # elif Which_Case == 1:
    #    with open("PlayerCase.txt", "w") as f:
    #       f.write(full_Response)


def getSuspects():
    global suspects
    global ccfReach
    global suspect_Count

    with open("CompleteCase.txt", 'r') as cc:
        lines = cc.readlines()

    for line in reversed(lines):
        if "CCF" in line:
            ccfReach = True
            break
        else:
            suspect_Count += 1
            suspects.append(line)
            print(line)
            
        

    #print(suspect_Count)

getSuspects()

Cfile = " "

print(f"\n{len(suspects)}")
i = 0
for s in range(len(suspects)):
    if not os.path.exists(f"Suspect/sp{i}.txt"):  
        Cfile = open(f"Suspect/sp{i}.txt", "x")
        f = open(f"Suspect/Logs/spl{i}.txt", "w")
    MakeCharacter(suspects[i], Cfile)
    i += 1


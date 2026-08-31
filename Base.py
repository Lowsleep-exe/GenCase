import ollama



def HeyLlama():
    prompt = input("What do you want ? \n")

    response = ollama.chat(model='tinyllama', messages=[
      {
        
        #"You are a Emotionally Intelligent AI helper. These are your emotions currently make sure they influence your response. Happiness:" + Happiness + " Co-Operation"+ Co_Op
        'role': 'system',
        'content': "You are an AI",
      },
      {
          'role': 'user',
          'content': prompt,

      }
    ])

      
    resp = response['message']['content']

    print(response['message']['content'])

    

    

HeyLlama()


     

    

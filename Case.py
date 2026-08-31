import ollama
import os

CCaseMake = ""
PCaseMake = ""
CCase = ""
if not os.path.exists('CompleteCase.txt'):  
  CCase = open("CompleteCase.txt", "x")

if not os.path.exists('PlayerCase.txt'):  
  PCase = open("PlayerCase.txt", "x")

with open("CompleteCaseCreator.txt", "r", encoding="utf-8") as file:
    CCaseMake = file.read()

with open("PlayerCaseCreator.txt", "r", encoding="utf-8") as file:
    PCaseMake = file.read()



print("Generating Case: \n")

def MakeCase(CaseInfo, Which_Case):

    if Which_Case == 0:

        system_prompt = """You are a STRICT COMPLETE CASE GENERATOR.

    You are generating the SECRET MASTER CASE FILE.

    You must follow EVERY instruction in the supplied Complete Case Creator prompt.

    The Complete Case Creator prompt defines the mystery, suspects, evidence,
    timeline, solution, deductions, and required output structure.

    IMPORTANT RULES:

    1. Generate EXACTLY 2 or 3 suspects.
    2. Generate the suspect names yourself.
    3. Use the EXACT SAME suspect names everywhere.
    4. There must be EXACTLY ONE perpetrator.
    5. The perpetrator must be one of the suspects.
    6. The mystery must be logically solvable.
    7. Every clue required to solve the mystery must exist in the case.
    8. Do not invent a fourth suspect.
    9. Do not use placeholder names.
    10. Do not change the solution halfway through writing.
    11. Complete the entire case before finishing.
    12. Include the COMPLETE SOLUTION.
    13. Include the DEDUCTION CHAIN.
    14. Include the FAIRNESS CHECK.
    15. Include the CCF SUSPECTS section.
    16. The CCF SUSPECTS section MUST be the FINAL section.
    17. NOTHING may appear after CCF SUSPECTS.
    18. CCF SUSPECTS must contain the actual suspect names generated in the case.
    19. Never reveal the perpetrator in the CCF SUSPECTS section.

    Before writing the case, privately determine:

    - perpetrator
    - motive
    - method
    - opportunity
    - timeline
    - evidence left behind
    - suspect lies
    - red herrings
    - deduction chain

    Then construct the case around that solution.

    Do NOT show private reasoning or hidden planning.

    Do NOT explain these instructions.

    OUTPUT ONLY THE COMPLETE CASE FILE.

    COMPLETE CASE CREATOR PROMPT:
    """ + CaseInfo

        user_prompt = """Generate the COMPLETE SECRET MASTER CASE now.

    Follow the supplied Complete Case Creator prompt exactly.

    Do not explain what you are doing.

    Do not discuss the prompt.

    Do not provide commentary.

    Output ONLY the completed case file."""
        

    elif Which_Case == 1:

        system_prompt = """You are a STRICT PLAYER CASE GENERATOR.

    You are generating the PLAYER-FACING CASE FILE for a detective mystery.

    You have been given a SECRET COMPLETE CASE MASTER FILE.

    Your job is to transform the complete case into a playable investigation.

    IMPORTANT:

    The COMPLETE CASE is the source of truth.

    DO NOT change:
    - the crime
    - the victim
    - the suspects
    - suspect names
    - evidence
    - timeline
    - locations
    - relationships
    - events
    - the perpetrator
    - the intended solution

    The player case must describe the SAME mystery.

    However, the player MUST NOT be told the solution.

    NEVER include:

    - the perpetrator's identity
    - the COMPLETE SOLUTION
    - hidden author notes
    - WHAT IT ACTUALLY MEANS
    - secret deductions that directly reveal the perpetrator
    - secret reasoning
    - private fairness analysis
    - author-only information
    - hidden suspect secrets unless the complete case says the player can discover them
    - any information that would spoil the answer

    The player must be able to solve the mystery using the information you provide.

    EVERY clue necessary to solve the mystery MUST remain available to the player.

    Do NOT remove evidence that is necessary for solving the case.

    Do NOT invent new evidence.

    Do NOT invent new suspects.

    Do NOT change suspect names.

    Do NOT change the number of suspects.

    Do NOT change the intended solution.

    Do NOT reveal which suspect is guilty.

    The player should receive enough information to independently determine the perpetrator.

    The case should feel like a realistic police investigation.

    Do not write explanations about how you converted the master case.

    Output ONLY the PLAYER-FACING CASE FILE.

    PLAYER CASE CREATOR PROMPT:
    """ + CaseInfo

        user_prompt = """Generate the PLAYER-FACING CASE now.

    Use the COMPLETE CASE MASTER FILE as the source of truth.

    Follow the supplied Player Case Creator instructions exactly.

    Remove secret solution information while preserving every clue necessary to solve the mystery.

    Do not reveal the perpetrator.

    Do not explain what you are doing.

    Do not discuss the prompt.

    Do not provide commentary.

    Output ONLY the playable case file."""

    response = ollama.chat(
        model='qwen2.5:3b', 
        messages=[
          {
            'role': 'system',
            'content':  system_prompt,
        },
        {
            'role': 'user',
            'content': user_prompt,
        }
        ],
        stream=True,
        options={
            'num_ctx': 8192, #4096 
            'num_predict': 3000
        }
      )

    full_Response = " "

    for chunk in response:
        text = chunk['message']['content']
        print(text, end="", flush=True)
        full_Response += text

    print("\n\n Finished")

    if Which_Case == 0:
      with open("CompleteCase.txt", "w") as f:
        f.write(full_Response)
    elif Which_Case == 1:
       with open("PlayerCase.txt", "w") as f:
          f.write(full_Response)

      
    

    # print(response['message']['content'])
    
PCaseMake += "\n \n" + CCase

MakeCase(CCaseMake, 0)
MakeCase(PCaseMake, 1)





     

    

import asyncio
import tokens
import assistant

async def WaitLoop(client: assistant.OpenAIChatHandler):
  while True:
    print("OpenAI GPT4o Assistant API Worked Example.\nType exit to quit.\n")
    
    prompt = input("USER: ")
    if prompt == "exit":
      await client.delete_thread()
      print("Exiting...")
      exit()
    
    print("\nWaiting for response.")
    response = await client.GenerateResponce(prompt)
    print("Responce returned.")
    
    print(f"\n{response}\n\n")
    
if __name__ == "__main__":
  toks = tokens.Keys()
  
  print(toks.openai_key)
  print(toks.assistant_id)
  
  client = assistant.OpenAIChatHandler(toks.GetAPIKey(), toks.GetAssistantId())
  asyncio.run(WaitLoop(client))
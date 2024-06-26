import openai
import asyncio

import tools

def parse_input(input_str):
    parts = input_str.split()
    text_parts = []
    image = None
    file = None
    
    i = 0
    while i < len(parts):
        if parts[i] == '--image':
            if i + 1 < len(parts):
                image = parts[i + 1]
            i += 2
        elif parts[i] == '--file':
            if i + 1 < len(parts):
                file = parts[i + 1]
            i += 2
        else:
            text_parts.append(parts[i])
            i += 1

    text = ' '.join(text_parts)
    
    return [text, image, file]

def GenerateResponce(prompt):
  return "Example Responce"

class OpenAIChatHandler:

  def __init__(self, openai_key: str, assistant_id: str):
    
    self.run = None
    self.ended = True
    
    self.openai_key = openai_key
    self.asssistant_id = assistant_id
    
    self.client = openai.OpenAI(api_key = openai_key)
    self.assistant = self.client.beta.assistants.retrieve(assistant_id)

  async def delete_thread(self):
    self.client.beta.threads.delete(self.run.thread_id)
    print("\n\nThread ended.")
    
  async def GenerateResponce(self, prompt):
    text, image, file = parse_input(prompt)
    
    thread_messages = []
    contents = []
  
    if image is not None:
      contents.append({"type": "text", "text": text})
      contents.append({"type": "image_url", "image_url": {"url": image}})
        
      thread_messages.append(
        {"role": "user", "content": contents}
      )
      
    else:
      thread_messages.append(
        {"role": "user", "content": text}
      )
    
    if self.run is None:
      self.run = self.client.beta.threads.create_and_run(
        assistant_id = self.assistant.id,
        thread = { "messages": thread_messages }
      )
      
    else:
      self.run = self.client.beta.threads.runs.create(
        thread_id = self.run.thread_id,
        assistant_id = self.assistant.id,
        additional_messages = thread_messages
      )
      
    response = await self.await_response()
    return response
  
  async def handle_tool_call(self):
    results = []
    for tool in self.run.required_action.submit_tool_outputs.tool_calls:
      result = await tools.handle_tool_call(tool)
      results.extend(result)
      
    self.run = self.client.beta.threads.runs.submit_tool_outputs(
      thread_id = self.run.thread_id,
      run_id = self.run.id,
      tool_outputs = results
    )
    
    await self.await_response()
      
  async def await_response(self):
    
    while not ((self.run.status == "completed")):# or (self.run.status == "requires_action")):
        
      match self.run.status:
        case "failed":
          await self.discorduser.dm_channel.send("Please let me (the user) know what happened if you're seeing this <3 - something went wrong that I didn't expect!")
          
        case "in_progress":
          #print("waiting for response...")
          await asyncio.sleep(0.35)
      
        case "requires_action":
          await self.handle_tool_call()
          
      self.run = self.client.beta.threads.runs.retrieve(thread_id = self.run.thread_id, run_id = self.run.id)
                                                        
    match self.run.status:
      case 'completed':
        
        messages = self.client.beta.threads.messages.list(
          thread_id = self.run.thread_id,
          limit = 2
        )
          
        result = messages.data[0].content[0].text.value
        
        return result
      
      case _:
        return "FAILED"
class Keys():
  def __init__(self):
    self.openai_key = ""
    self.assistant_id = ""
    
    with open("tokens.txt") as file:  
      self.openai_key = file.readline().strip("\n")
      self.assistant_id = file.readline().strip("\n")
      
  def GetAPIKey(self) -> str:
    return self.openai_key
  
  def GetAssistantId(self) -> str:
    return self.assistant_id
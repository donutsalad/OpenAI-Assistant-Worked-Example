import json
import example_functions

tool_list = [
  { "tool_id": "test_run", "method": example_functions.SimpleTestRun },
  { "tool_id": "get_weather", "method": example_functions.GetWeather }
]

async def handle_tool_call(call):
  args = json.loads(call.function.arguments)
    
  for method in tool_list:
    if method["tool_id"] == call.function.name:
      return [{
        "tool_call_id": call.id,
        "output": method["method"](args)
      }]
      
  return [{
    "tool_call_id": call.id,
    "output": "Please let the user know that this tool isn't implemented yet"
  }]
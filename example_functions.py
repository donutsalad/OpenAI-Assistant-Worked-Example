def SimpleTestRun(tool_args):
  return "Let the user know this was a successful test run."

def GetWeather(tool_args: dict):
  unit = tool_args.get("unit", "c")
  match unit:
    case "c":
      return f"The weather in {tool_args["location"]} is 32C"
    case "f":
      return f"The weather in {tool_args["location"]} is 90F"
    case _:
      return "Let the user know that the unit of measurement is unrecognised"
# OpenAI Worked Example for the Assistant API

Short readme for now. More detailed doccumentation on it's way!

This is a simple cli implementation of the Assistant API to make creating your own python clients just that much easier.
I plan to create doccumentation explaining what each part of the code does, adding features like file upload and vision soon.
Once you play around with the cli code you can just copy paste the code into your own project - whatever interface you choose!

Vision has been implemented as an arg in the user input, an example usage would be:

`USER: hey! what dog breed is this? --image https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg`

File search functionality has also been implemented, an example usage would be:

`USER: hey can you explain the parameters in get_weather? --file tool_calls/get_weather.json`

Let me know if you want new features added, I'm more than happy to implement it to make everyones experiments easier!

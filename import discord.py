import discord
import requests

# Replace TOKEN with the token for your bot account
client = discord.Client(token="")

# This function will be called when the bot receives a message
@client.event
async def on_message(message):
    # Ignore messages that are sent by the bot itself
    if message.author == client.user:
        return

    # If the message contains an image attachment, remove the background
    if message.attachments:
        attachment = message.attachments[0] # Get the first attachment from the message
        image_url = attachment.url # Get the URL of the image
        image_data = requests.get(image_url).content # Download the image
        api_key = "b18838a9-7083-4943-b586-bd0e0a3b5dbe" # Your Benzin API key
        response = requests.post(
            "https://api.benzin.io/background",
            files={"image": image_data},
            headers={"X-API-KEY": api_key},
        )
        result = response.json() # Get the response from the API as JSON
        # Check if the API call was successful
        if result["status"] == "success":
            # Get the URL of the resulting image with the background removed
            image_url = result["result"]["url"]
            # Send the resulting image back to the channel
            await message.channel.send(image_url)
        else:
            # If the API call failed, send an error message back to the channel
            await message.channel.send("Failed to remove the background of the image")
#hi
# Run the bot
client.run()

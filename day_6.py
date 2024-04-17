
def emoji_converter(message):
    final_message = []
    
    message_arr = message.split()
    
    def get_emoji(text):
        final_emoji = ""
        
        faces = {
        ":|": "😐",
        ":)": "😊",
        ":(": "😔"
        }
        
        for shape, emoji in faces.items():
            if shape == text:
                final_emoji = emoji
                break
            else:
                final_emoji = text
        
        return final_emoji
   
   
    def get_emoji_from_text(text):
        final_emoji = ""
        
        faces = {
        "excited": "😐",
        "happy": "😊",
        "sad": "😔",
        }
        
        for shape, emoji in faces.items():
            if shape.lower() == text.lower():
                final_emoji = emoji
                break
            else:
                final_emoji = text
        
        return final_emoji


    for each_text in message_arr:
        if len(get_emoji(each_text)) == 1:
            final_message.append(get_emoji(each_text))  
        else:
            final_message.append(get_emoji_from_text(each_text))  
            
  
    return " ".join(final_message)


query = input("Insert your text:\n")

print(emoji_converter(query))
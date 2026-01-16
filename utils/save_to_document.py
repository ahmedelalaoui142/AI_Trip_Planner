import os
import datetime

def save_document(response_text:str,directory: str= "./output"):
    """Save the response text to a document"""
    os.makedirs(directory,exist_ok=True)
    markdown_content = f"""# Trip Plan
    \n\n{response_text}
    ____
    This is AI generated travel plan, please verify the information :)
    """
    
    try:
       timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
       file_name = f"{directory}/trip_plan_{timestamp}.md"
       with open(file_name,"w",encoding="utf-8") as f:
        f.write(markdown_content)
        print(f"Document saved as {file_name}")
       return file_name
    except Exception as e:
       print(f"Failed to save document: {e}")
       return None
                       
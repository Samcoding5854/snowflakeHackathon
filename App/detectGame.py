import streamlit as st
import replicate

REPLICATE_API_TOKEN = "r8_JLosWfgzJu6KExgiR5Efdq9JEDVxKCg2M9gsp"

import json
# Function to call LLM API and get story response
def call_llm_api():
    input_data = {
        "prompt": '''You are a part of a detective game where a player needs to solve a murder mystery. Provide a detailed response in JSON format that includes the following sections:

        1. **Story:** Provide a captivating and detailed narrative describing the murder and the scene. Include information about the victim's background, recent activities, relationships, and any suspicious events leading up to the murder.

        2. **Suspects:**
        - **Name:** 
        - **Alibi:** 
        - **Background:** 
        - **Motive:** 
        - **Relationship with the Victim:** 

        3. **Hints:** Offer a series of hints that can be revealed incrementally to guide the player in their investigation. These hints should be relevant to the story and suspects, providing subtle clues without giving away the solution outright.

        4. **Solution:** Provide a simplified solution with only the name of the murderer and a brief explanation of why they are the suspect. Highlight key pieces of evidence or motives that incriminate the chosen suspect, reinforcing the player's deduction process.

        Ensure the information is clear, immersive, and organized in the JSON format for an engaging user experience.''',

    "temperature": 0.2,
    "max_new_tokens":1024
    }

    api = replicate.Client(api_token=REPLICATE_API_TOKEN)
    output = api.run("snowflake/snowflake-arctic-instruct", input=input_data)
    output_text = "".join(output)
    print(output_text)
    return output_text

# Main function
def detect_Game():
    st.title("Detective Game")

    # Button to trigger API call and display story
    if st.button("Generate Story"):
        # Call LLM API to get story response
        response = call_llm_api()
        response = json.loads(response)

        # Display Story
        st.header("The Murder Case")
        st.write(response["Story"])

        # Display Suspects in Cards
        st.subheader("Suspects")
        cols = st.columns(len(response["Suspects"]))  # Create columns based on number of suspects

        for i, suspect in enumerate(response["Suspects"]):
            with cols[i]:
                st.write(f"**Suspect {i+1}: {suspect['Name']}**")  # Start numbering from 1
                st.write(f"Alibi: {suspect['Alibi']}")
                st.write(f"Background: {suspect['Background']}")
                st.write(f"Motive: {suspect['Motive']}")
                st.write(f"Relationship with Victim: {suspect['Relationship with the Victim']}")

        # Display Hints
        st.subheader("Hints")
        with st.expander("See Hints"):
            for i, hint in enumerate(response["Hints"], start=1):
                st.write(f"Hint {i}: {hint['Hint '+str(i)]}")  # Access hint using string formatting
        # User Selection and Solution
        if "murderer_selected" not in st.session_state:  # Check if key doesn't exist
            st.session_state["murderer_selected"] = None  # Set default to None

        suspect_names = [""] + [suspect["Name"] for suspect in response["Suspects"]]  # Add an empty string

        murderer_selected = st.selectbox("Who is the murderer?", suspect_names, key="murderer_selected")

        if murderer_selected is None:  # Check if empty string is selected (no selection)
            st.write("Select a suspect to reveal the answer.")
        elif murderer_selected == response["Murderer"]:
            st.success("Congratulations! You solved the case.")
            st.write(response["Explanation"])
        else:
            st.error(f"Oops! That seems to be incorrect. The murderer was actually {response['Murderer']}.")
            st.write(response["Explanation"])
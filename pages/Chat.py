import streamlit as st

# Set up the page
import streamlit as st

# Set up the page
st.title("Climate Policy Chat")

# Display the conversation
with st.container():
    st.subheader("Conversation")

    # Question 1
    st.write("**Q:** What recent actions has California taken to address climate change?")
    st.write("**A:** California has been at the forefront of climate change and green policies in the United States. In 2022, the state made significant strides in its climate action plan. Under the California Climate Commitment, the state aims to achieve net zero carbon pollution by 2045, with an 85% reduction in greenhouse gas emissions as part of that goal. This ambitious plan also includes creating 4 million new jobs and cutting air pollution by 71%. Governor Gavin Newsom emphasized the urgency of taking action against climate change and the state's commitment to slashing air pollution, transitioning to clean energy, and protecting communities from climate-driven crises like wildfires and drought.")

    # Question 2
    st.write("**Q:** How are California's representatives contributing to climate change policies?")
    st.write("**A:** Representative Jimmy Panetta of California's 19th Congressional District has been active in advancing legislation to address climate change. He supports investments in clean energy and policies that prioritize community health and safety. Panetta has authored and cosponsored legislation to block oil drilling in oceans and reduce carbon emissions.")

    # Question 3
    st.write("**Q:** What measures is California taking to involve corporations in climate action?")
    st.write("**A:** California has also taken steps to hold corporations accountable for their role in climate change. New laws require U.S. companies with annual revenues of $1 billion or more to report their direct and indirect greenhouse gas emissions. This move is expected to have a global impact and could influence federal U.S. policies.")

# Optionally, you could add an input box to simulate user typing a response
user_input = st.text_input("Your response", placeholder="Type here...")

# You can use the user input to continue the conversation or for other purposes in your app
if user_input:
    st.markdown(f"**You:** {user_input}")

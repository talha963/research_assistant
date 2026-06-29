import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv

load_dotenv()

class ResearchReport(BaseModel):
    report_content: str = Field(description="The detailed, multi-section final report. Formatted in markdown.")
    confidence_score: int = Field(description="A confidence score from 1 to 100")
    citations: list[str] = Field(description="A list of sources or citations used")

st.set_page_config(page_title="Agentic Research Assistant", layout="centered")
st.title("🕵️‍♂️ Agentic Research Assistant")

llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0.2)

json_llm = llm.bind(response_format={"type": "json_object"})

query = st.text_input("What topic would you like me to research for you?")

if st.button("Start Research") and query:
    st.info("🧠 Step 1: Planning the research strategy...")
    planner_prompt = ChatPromptTemplate.from_template(
        "You are a master research planner. Break this user query into 3 specific steps to research: {query}"
    )
    plan = (planner_prompt | llm).invoke({"query": query}).content
    with st.expander("View Research Plan"):
        st.write(plan)

    st.info("🔍 Step 2: Executing the research plan...")
    research_prompt = ChatPromptTemplate.from_template(
        "You are a researcher. Execute this plan and gather all the necessary facts: {plan}"
    )
    research_data = (research_prompt | llm).invoke({"plan": plan}).content
    with st.expander("View Raw Research Data"):
        st.write(research_data)

    st.success("📝 Step 3: Structuring final report with confidence scores...")
    
    parser = PydanticOutputParser(pydantic_object=ResearchReport)
    
    synth_prompt = ChatPromptTemplate.from_template(
        "You are a professional writer. Turn this raw data into a report.\n\n"
        "Raw Data: {research_data}\n\n"
        "{format_instructions}\n\n"
        "CRITICAL INSTRUCTION: Output ONLY a valid JSON object. Do not include any conversational text, markdown formatting blocks (like ```json), or preambles. Ensure all strings inside arrays are enclosed in double quotes."
    )
    
    final_chain = synth_prompt | json_llm | parser
    
    final_output = final_chain.invoke({
        "research_data": research_data,
        "format_instructions": parser.get_format_instructions()
    })
    
    st.markdown("---")
    st.markdown("### Final Research Report")
    st.markdown(final_output.report_content)
    
    st.metric(label="AI Confidence Score", value=f"{final_output.confidence_score}%")
    
    st.markdown("**Citations:**")
    for citation in final_output.citations:
        st.markdown(f"- {citation}")
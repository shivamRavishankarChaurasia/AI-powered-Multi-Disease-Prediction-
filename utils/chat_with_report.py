from langchain_community.llms import LlamaCpp
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain  # ✅ Updated import

llm = LlamaCpp(
    model_path=r"D:\abcdefghj\Projects\AI_Powered_Multi_Disease\model_weights\mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_gpu_layers=20,
    n_batch=256,
    n_ctx=2048,
    temperature=0.7,
    top_p=0.95,
    verbose=False,
)

template = """
You are a medical assistant. Here's the patient's medical report:

{report}

Answer the user's question:
{question}
"""

prompt = PromptTemplate(
    input_variables=["report", "question"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

def chat_with_report(report_text, user_question):
    response = chain.run(report=report_text, question=user_question)
    return response

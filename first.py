from langchain.llms import OpenAI
# Secure this key!
api_key="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"

llm=OpenAI(
    openai_api_key=api_key,
)

result=llm("Write a very very short poem ")
print(result)